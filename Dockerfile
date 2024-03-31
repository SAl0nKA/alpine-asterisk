FROM alpine:latest
RUN apk update

RUN apk add asterisk
RUN apk add --no-cache python3 py3-pip py3-dotenv nano net-snmp-tools asterisk-sounds-en