FROM alpine:latest
RUN apk update
#alpine-sdk
#RUN apk add build-base

#RUN apk add g++ make gcc 
#RUN apk add git jansson-dev sqlite-dev libedit-dev libuuid

RUN apk add asterisk
RUN apk add --no-cache python3 py3-pip py3-dotenv nano net-snmp-tools asterisk-sounds-en
#RUN pip3 install python-dotenv
#RUN python3 -m venv /opt/scripts
#RUN chmod +x /opt/scripts/bin/activate
#RUN . /opt/scripts/bin/activate
#RUN pip install python-dotenv
#RUN . /opt/scripts/bin/deactivate
#RUN apk add task taskd taskd-pki task-doc taskd-doc

#gcc build-essential
#RUN apk add git-core libsqlite3-dev uuid-dev libedit-dev build-essential wget libxml2-dev libjansson-dev


#WORKDIR /opt
#RUN wget http://downloads.asterisk.org/pub/telephony/asterisk/asterisk-20-current.tar.gz

#RUN mkdir /opt/asterisk
#RUN tar -xvzf asterisk-20-current.tar.gz -C /opt/asterisk
#WORKDIR /opt/asterisk/asterisk-20.6.0

#RUN ls
#RUN apk add tree
#RUN tree /opt
#RUN cd $(find . -type d -name "asterisk-20.*" | head -n 1)
#RUN target_dir=$(find . -type d -name "asterisk-20.*" | head -n 1) && \
#    test -n "$target_dir" && \
#    test -e "/opt/asterisk" || ln -s "$target_dir" /opt/asterisk

#RUN pwd
#RUN ls -la
#RUN ./configure --without-pjproject-bundled 
#RUN make -j2 
#RUN make install
#RUN make samples
#RUN make config
#RUN make install-logrotate

#WORKDIR /home/niki/asterisk
#RUN rm -rf /home/niki/asterisk-14-current*


#RUN apt install iputils-ping -y


#EXPOSE 5060/udp 5060 5061 10000-10099/udp

#CMD ["asterisk", "-f"]


#CMD touch /etc/asterisk/woman && 
#CMD ls /etc/asterisk

#CMD asterisk -fvvvvvvvv
