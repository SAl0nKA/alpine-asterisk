#!/bin/sh
ip_output="$(ip a)"
docker_eth_ip=$(echo "$ip_output" | grep -A 3 "eth1" | awk '/inet / {print $2}')
sed -i "s#docker_ip#$docker_eth_ip#g" /etc/asterisk/pjsip.conf