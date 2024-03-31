# Alpine Asterisk

This repository contains Docker files to create an Asterisk instance in a Docker container and Python scripts which can create sample config files and users.

## Getting Started

To get started with this project, follow these steps:

### 1. Clone the Repository

Clone this repository to your local machine using Git:

```bash
git clone https://github.com/SAl0nKA/alpine-asterisk.git
```

### 2. Create .env file

Before building and starting the container you need to create .env file with users in the scripts folder. The format has to be like this:
```bash
NAME0=somename
PASSWORD0=somepassword
MD50=true
NAME1=somename
PASSWORD1=somepassword
MD51=false
NAMEx=somename
PASSWORDx=somepassword
MD5x=true
```
where x is the number of the user starting from 0. If you don't want to create any users leave the file empty.

### 3. Build the container
You can find how to install Docker on the official Docker site [here](https://docs.docker.com/engine/install/).

Start container using:
```bash
docker compose up -d
```

You can connect directly to the container
```bash
docker exec -it alpine-asterisk /bin/sh
```
or directly to the Asterisk
```bash
docker exec -it alpine-asterisk asterisk -rvvvvvvv
```

### 4. Check the config files
After starting the container you should see the config files under `/etc/asterisk` either on your host machine or in the container.


## Troubleshooting
### Missing Asterisk packages
Alpine Linux Asterisk is pretty lightweight so you'll probably miss some packages. You can view them [here](https://pkgs.alpinelinux.org/package/edge/main/x86/asterisk) under Sub packages. If you spot one you need just add it to the `Dockerfile` and rebuild the image
```bash
docker compose build
docker compose down
docker compose up -d
```

### Missing paths for Asterisk
You can add another path in `docker-compose.yml` under volumes if you're missing some files from your host machine
```dockercompose
"/path/on/your/host:/path/in/your/container:rw"
```

