from dotenv import load_dotenv
import hashlib
import os

CONFIG_PATH = "/etc/asterisk/pjsip.conf"


class User:
    def __init__(self, name, password, md5=False):
        self.name = name
        self.md5 = md5
        self.password = self.get_password_hash(password)

    def get_password_hash(self, password):
        if self.md5:
            return hashlib.md5(f"{self.name}:asterisk:{password}".encode()).hexdigest()
        else:
            return self.password

    def print_user(self):
        print(f"{self.name}\n{self.password}\n")

    def get_user_pjsip_config(self):
        return f"""[{self.name}]
type=endpoint
transport=transport-udp-ipv4
context=dokovanie
disallow=all
allow=ulaw
allow=alaw
auth={self.name}
aors={self.name}

[{self.name}]
type=aor
max_contacts=5

[{self.name}]
type=auth
auth_type={"md5" if self.md5 else "userpass"}
username={self.name}
password={self.password}
"""

    def write_to_config(self):
        try:
            with open(CONFIG_PATH, 'a') as file:
                file.write(self.get_user_pjsip_config())
            print(f"Config for user {self.name} successfully written")
        except FileNotFoundError:
            print("pjsip.conf file not found")


def count_lines_in_file():
    line_count = 0
    with open(".env", 'r') as file:
        for _ in file:
            line_count += 1
    return line_count


def main():
    os.system("pwd")
    os.system("ls -la")
    load_dotenv()
    num_of_lines = count_lines_in_file()
    if num_of_lines % 3 != 0:
        print("Bad .env file, exiting")
        return

    num_of_users = int(num_of_lines / 3)
    print(f'Found {num_of_users} {"user" if num_of_users == 1 else "users"}')
    with open(CONFIG_PATH, 'r') as file:
        content = file.read()

        for i in range(num_of_users):
            user = User(os.getenv(f"NAME{i}"), os.getenv(f"PASSWORD{i}"), os.getenv(f"MD5{i}"))
            i += 1

            found_at = content.find(f"[{user.name}]")
            if found_at != -1:
                print(f"User {user.name} found in the existing config, skipping.")
                return

            user.write_to_config()


#         todo upravenie do pjsip.conf


if __name__ == '__main__':
    main()
    print("Done")
