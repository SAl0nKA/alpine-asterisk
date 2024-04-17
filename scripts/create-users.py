from dotenv import load_dotenv
import hashlib
import os

CONFIG_PATH = "/etc/asterisk/pjsip.conf"
#for testing purposes
# CONFIG_PATH = "./config/pjsip.conf"


class User:
    def __init__(self, name, password, md5=False):
        self.name = name
        self.md5 = md5
        self.password = self.get_password_hash(password)

    def get_password_hash(self, password):
        if self.md5:
            return hashlib.md5(f"{self.name}:asterisk:{password}".encode()).hexdigest()
        else:
            return password

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

    def write_to_config(self, file):
        file.write(self.get_user_pjsip_config())
        print(f"Config for user {self.name} successfully written.")


def main():
    load_dotenv()
    env_variables = os.environ

    with open(CONFIG_PATH, 'r+') as file:
        content = file.read()

        i = 0
        stop_condition = False

        while not stop_condition:
            name_key = f"NAME{i}"
            password_key = f"PASSWORD{i}"
            md5_key = f"MD5{i}"
            i += 1

            if name_key in env_variables:
                name_value = os.getenv(name_key)
                password_value = os.getenv(password_key)
                if password_value is None:
                    print(f"Password for user {name_value} not set, skipping.")
                    continue
                md5_value = os.getenv(md5_key)
                if md5_value is None:
                    print(f"MD5 for user {name_value} not set, using plain text password.")
                    md5_value = False

                user = User(name_value, password_value, md5_value)
                found_at = content.find(f"[{user.name}]")
                if found_at != -1:
                    print(f"User {user.name} found in the existing config, skipping.")
                    continue

                user.write_to_config(file)
            else:
                stop_condition = True


if __name__ == '__main__':
    main()
    print("Done")
