#!/bin/bash

if [[ $EUID -ne 0 ]]; then
	echo "You must be root"
	echo "Do: $ ./sudo ${0}"
fi

echo -e "Updating system and python packages......\n\n"

sleep 0.5

apt-get update && apt-get install python3 python3-pip -y
pip3 install -r requirements.txt

echo -e "\n\nCopying files......\n\n"

sleep 0.5

cp ./lib/instapeek.py /usr/lib/python3.9/
cp ./src/instapeek-tool.py /usr/local/bin/instapeek
chmod +x /usr/local/bin/instapeek

echo -e "Done.\nUse command to start:\n\n$ instapeek"
