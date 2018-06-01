#!/usr/bin/python3

import os

# Search folder in a current location 

def openfile():
	fo=open(search,'r+')
	g=fo.read()
	print(g)
	fo.close()

search=input("enter Folder name")

#fi=input("enter file name")
file1=search.capitalize() #......to make first letter of a word in upper case

file2=search.upper()  #.... to convert whole string into upper case

#filename=[file1,file2]

#for filename in os.listdir(os.getcwd(search)):

if os.path.exists(search) == True :

	print("YES Folder Exists here")
		
	openfile()
	
elif  os.path.exists(file1) == True :
		
	print("does exists")
	
	openfile()

elif  os.path.exists(file2) == True :

	print("does exists")
	
	openfile()
else :
	print("Doesnot exist")




