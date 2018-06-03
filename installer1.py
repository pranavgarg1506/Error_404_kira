#!/usr/bin/python3
import speech_recognition as sr
import subprocess as su
import os

#get the audio from microphone
r = sr.Recognizer()
mic = sr.Microphone()
final_txt=[]
with mic as source:

	r.adjust_for_ambient_noise(source)
	print("which module you want to install...?")
	audio= r.listen(source)#... store audio into the variable


	try:
		speak=r.recognize_google(audio)
		strip_txt=speak.strip()
		final_txt=strip_txt.split()
		print(final_txt)
	
		
		if 'install' in final_txt:
			for i in range(0,len(speak)):
				if final_txt[i]=='install':
					module_name=final_txt[i+1]
					break

		print("In which platform u want to install")
		print("1.python")
		print("2.python3")
		print("choose option(in number)")# enter the value in text form.
		
		ch=input()
		if ch=='Python'or'1':
			s="sudo pip" + " " + "install" + " " + module_name
			os.system(s)		

		if ch=='Python3'or'2':
			s="sudo pip3" + " " + "install" + " " + module_name
			os.system(s)
			
		else:
			s="sudo apt-get" + " " + "install" + " " + module_name
			os.system(s)


		

	except:
		print("Could not understand your voice")




























