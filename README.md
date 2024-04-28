# Alpine Asterisk

This repository contains Docker files needed to create an Asterisk instance in a Docker Swarm and Python scripts which can create sample config files and users.

## Getting Started
To get started with this project, follow these steps:

### 1. Clone the Repository

Clone this repository to your local machine using Git:

```bash
git clone https://github.com/SAl0nKA/alpine-asterisk.git
```

### 2. Create Docker Swarm
You can find how to install Docker on the official Docker site [here](https://docs.docker.com/engine/install/).


To initialize Docker Swarm run this command on your machine which you want to act as a swarm manager:
```
docker swarm init --advertise-addr <your-machine-ip>
```
This will return a command which you can use on your other machines that will act as worker nodes
```
docker swarm join --token <token> <your-machine-ip>:2377
```

### 3. Create .env file
Before building and starting the container you need to create .env file with swarm manager IP and Asterisk endpoints in the scripts folder. The format has to be like this:

```bash
MANAGER_IP=x.x.x.x
NAME0=somename
PASSWORD0=somepassword
MD50=true
NAME1=somename
PASSWORD1=somepassword
NAMEn=somename
PASSWORDn=somepassword
MD5n=true
```
where n is the number of the user starting from 0. If you don't want to create any users you can omit the user fields.

### 4. Create local registry
For worker nodes to be able to get your newest image you'll need to create a local registry where you'll upload the newest image. Create the registry with 
```
docker service create --name registry --publish published=5000,target=5000 registry:2
```

**NOTE:** If you have your own config files put them into the `config` folder and edit the `docker-compose.yml` configs section to match your files.

Don't forget to paste these lines in your transport templates inside `pjsip.conf`. Script `parseIP.sh` uses these keywords to set a correct IP addresses inside the swarm.
```
;####################
local_net=docker_ip
external_media_address=external_ip
external_signaling_address=external_ip
;####################
```

Now you can build the image with
```
docker build -t <manager-ip>:5000/alpine-asterisk
```
and push 
```
docker push <manager-ip>:5000/alpine-asterisk
```

**NOTE:** If your worker nodes won't be able to pull the image because of https error you'll need to add the following lines into `/etc/docker/daemon.json` and restart the Docker Engine
```
{
  "insecure-registries": ["<manager-ip>:5000"]
}
```

### (Optional) Running portainer
For better visualisation and management of the swarm you can run portainer with command

```
docker run -d -p 8000:8000 -p 9443:9443 --name=portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce
```

You can then connect with your web browser to `<manager-ip>:9443` where you'll need to create a password with at least 12 characters. After that you'll be able to see all Docker options.

### 5. Deploying stack
To deploy the stack use
```bash
docker stack deploy asterisk -c docker-compose.yml
```

You can check the status of the running container with portainer or with 
```
docker stack ps asterisk
```

After making changes to the docker-compose.yml you can update the stack using the same stack deploy command. 

However, if you've changed your config files you'll need to remove the stack with
```
docker stack rm asterisk
```
and then redeploy it to update the Docker configs.

## Using the Asterisk
 After successfully deploying the stack you can now connect to the Asterisk with your VoIP phone. As the SIP server address use your swarm manager IP and use the user credentials you specified in the `.env` file.

In the current version of the project it is only possible to use one Asterisk instance at the time because of default load-balancing which Docker Swarm provides. To fix this you can use some sort of proxy such as Kamailio to evenly distribute the traffic.

## Troubleshooting
### Missing Asterisk packages
Alpine Linux Asterisk is pretty lightweight so you'll probably miss some modules. You can view them [here](https://pkgs.alpinelinux.org/package/edge/main/x86/asterisk) under Sub packages. If you spot one you need just add it to the `Dockerfile` and rebuild the image


### Debugging Asterisk
You can connect directly to the running container on your manager node with
```bash
docker exec -it asterisk... /bin/sh
```
or directly to the Asterisk
```bash
docker exec -it asterisk... asterisk -rvvvvvvv
```
**NOTE:** The name of the running container will contain some generated ID. You can use Tab to fill in the full name.

The images contain tools such as sngrep and nano to easily debug the SIP traffic.

### Changing endpoint template
You can find the template for user endpoints in `scripts/create-users.py` where you can change it according to your needs.