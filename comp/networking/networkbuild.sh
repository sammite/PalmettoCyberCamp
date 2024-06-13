#/bin/bash

# Code to automate network traffic generation
#
# pass a comms over a raw TCP connection


printf "hello my name is PCSC-NETCAT-FLAG-PCSC" | nc 192.168.2.5 456


# Telnet and connect to a sus telnet server

telnet 10.10.10.10

# Pass a 7zipped file over UDP connection

cat  file.7z | netcat 172.16.12.4 8000 -w 1


# ncat -vl -p 8000 > file.foo

# Pass a Meme over the network connection
#

curl http://10.10.10.4:8080/meme.png


# Pass a nice cookie over the network with a PCSC flag
curl --cookie "name=$(echo 'PCSC-CAN-I-HAS-COOKIE-PCSC' | base64 )" google.com




