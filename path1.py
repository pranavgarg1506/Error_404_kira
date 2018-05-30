#!/usr/bin/python3
#voice recognition
import os
import speech_recognition as sr 
import subprocess                                                              
r = sr.Recognizer()
path="/"
final="/home/"+subprocess.getoutput("whoami")
c=[] 
f=0   
d=""                                                                              
with sr.Microphone() as source: 
	r.adjust_for_ambient_noise(source) # here                                                                      
	print("Speak:")                                                                                   
	audio = r.listen(source)
try:
	a=(r.recognize_google(audio))
	#if path is at current location
	if (a=="current location") or (a=="current path") or (a=="present location") or (a=="present path") or (a=="here"):
		final=subprocess.getoutput("pwd")
	#if path is a somewhere else in user
	else:
		b=a.split()
		if ("on" in b) or ("in" in b) or ("at" in b):
			for i in range(0, len(b)):
				if (b[i]=="on") or (b[i]=="in") or (b[i]=="at"):
					c.insert(len(c),b[i+1])
					for j in range(0, len(c)):
						d=(path+c[j])
						final=(final+d)
						d=""
						c=[]
	print(final)
except:
	print("Could not understand audio")
	pass
