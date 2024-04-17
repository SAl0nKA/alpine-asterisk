FROM alpine:latest

RUN apk update
RUN apk add asterisk asterisk-sounds-en
RUN apk add --no-cache python3 py3-pip py3-dotenv
#for debugging purposes
RUN apk add nano sngrep

WORKDIR /opt/scripts
ADD ./scripts/* /opt/scripts
#todo add using docker compose env
ADD ./scripts/.env /opt/scripts
RUN chmod +x parseIP.sh
WORKDIR /opt/config

#WORKDIR /etc/asterisk
#ADD ./config/* /etc/asterisk

WORKDIR /
ADD ./entrypoint.sh /
RUN chmod +x entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]


#compilation attempts

#RUN apk add busybox-binsh c-client libcap2 libcrypto3 libcurl libedit libgcc
#RUN apk add libssl3 libuuid libxml2 lua5.1-libs musl portaudio sqlite-libs unbound-libs zlib libedit-dev patch
#RUN apk add g++ make gcc
#RUN apk add uuidgen util-linux-dev libxml2-dev sqlite-dev
#RUN apk add git jansson-dev sqlite openssl
#RUN apk add pjproject-dev
#RUN apk add pjproject jansson

#https://github.com/ipoddubny/alpine-asterisk/blob/master/15/Dockerfile
#RUN apk update \
#  && apk add libtool libuuid jansson libxml2 sqlite-libs readline libcurl libressl zlib libsrtp lua5.1-libs spandsp unbound-libs \
#  && apk add --virtual .build-deps gnupg build-base patch bsd-compat-headers util-linux-dev ncurses-dev libresample \
#        jansson-dev libxml2-dev sqlite-dev readline-dev curl-dev libressl-dev unbound-dev \
#        zlib-dev libsrtp-dev lua-dev spandsp-dev

#WORKDIR /opt
#RUN wget -O asterisk.tar.gz http://downloads.asterisk.org/pub/telephony/asterisk/asterisk-20-current.tar.gz
#RUN tar -xzf asterisk.tar.gz -C /opt
#RUN rm asterisk.tar.gz
#RUN mv asterisk* asterisk
#WORKDIR /opt/asterisk

#RUN contrib/scripts/install_prereq install
#RUN ./configure --without-pjproject-bundled --without-jansson-bundled
#RUN make menuselect.makeopts
#RUN ./menuselect/menuselect --disable BUILD_NATIVE menuselect.makeopts \
#    --disable astdb2sqlite3 \
#    --disable astdb2bdb
#make clean
#make distclean
#RUN make
#RUN make -j 2
#RUN make install 
#RUN make samples
#RUN make config
#RUN make install-logrotate


#EXPOSE 5060/udp 5060 5061 10000-10099/udp

#CMD ["asterisk", "-f"]
