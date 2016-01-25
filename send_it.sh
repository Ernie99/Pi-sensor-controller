#!/bin/bash

echo "start send of python file"

sshpass -p "password" scp pi_SHT31.py pi@r1.local:/home/pi/pi_SHT31.py

echo "send completed"
