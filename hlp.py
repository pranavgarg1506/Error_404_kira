#!/usr/bin/env python3
import speech_recognition as sr                                                                    
r = sr.Recognizer()                                                                                   
with sr.Microphone() as source: 
	r.adjust_for_ambient_noise(source) # here                                                                      
	print("Speak:")                                                                                   
	audio = r.listen(source)  
 
try:
	a=r.recognize_google(audio)
	b= a.split()
	if ("help" in b) and ("directory" in b):
		print("Hello this is kira. i can perform multiple directory operations")
		print("1) create a directory")
		print("2) delete a directory")
		print("3) rename a directory")
		print("4) move a directory")
		print("5) copy a directory")
		print("6) empty a directory")
		print("7) properties a directory")
		print("8) List of all directories in a path")
		print("9) List of all files in the directory")
		print("10) Number of files in a directory")
		print("11) Searching a file in a directory")
		print("12) Search a directory in a path")
		print("13) Open a file in a directory")
		print("14) Permissions of all files in a directory")
		print("15) Show all hidden Folders")
		print("16) Hiding a folder")
		print("17) showing Breanch system of a directory")
		print("18) create a shortcup of a directory")
except:
	print("Could not understand audio")
	pass
