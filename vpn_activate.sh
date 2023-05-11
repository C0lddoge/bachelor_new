#!/bin/bash
read -p "One time password: " otpass
f5fpc -s -t vpn.univie.ac.at -u moserk01@${otpass} -d /etc/ssl/certs/
sleep 5
f5fpc --info



