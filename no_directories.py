#!/usr/bin/python3
count=0
import os
a="/home/ashit/Desktop"
os.system("ls -l "+a+" | grep -c ^d")
