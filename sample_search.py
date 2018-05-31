#!/usr/bin/python3

import os

# Search folder in a current location 

search=input("enter Folder name")
file=search.capitalize() #......to make first letter of a word in upper case

file2=search.upper()  #.... to convert whole string into upper case

if os.path.exists(search) == True :
	
	print("YES Folder Exists here")
	
elif  os.path.exists(file) == True :
	
	print("does exists")

elif  os.path.exists(file2) == True :
	print("does exists")

else :
	print("Doesnot exist")
