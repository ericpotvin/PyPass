#!/bin/bash

if [ -z "$1" ]; then
	echo "ERROR: A string is required!"
elif [ -z "$2" ]; then
	echo "ERROR: A password is required!"
elif [ -z "$3" ]; then
	echo "ERROR: A cipher is required!"
else
	echo "$1" | /usr/bin/openssl enc -"$3" -base64 -d -pass pass:"$2"
fi
