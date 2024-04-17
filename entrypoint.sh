#!/bin/sh
#copy files because of read-only restrictions
cp /opt/config/* /etc/asterisk/ &&
#change their permission to be able to write to them
chmod 700 /etc/asterisk/* &&
#run script to create sample configs if none are present
python3 /opt/scripts/create-sample-config.py &&
#run script to create users from env variables
python3 /opt/scripts/create-users.py &&
#change the local IP address inside pjsip.conf because of Docker networking
/bin/sh /opt/scripts/parseIP.sh &&
#run Asterisk in foreground so the container doesnt stop
asterisk -f