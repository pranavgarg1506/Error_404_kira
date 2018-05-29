#!/usr/bin/python3
import speech_recognition as sr
import subprocess as su
import os

#get the audio from microphone
r = sr.Recognizer()
mic = sr.Microphone()

with mic as source:

	r.adjust_for_ambient_noise(source)
	print("move operation on file")
	audio= r.listen(source)#... store audio into the variable


	try:
		speak=r.recognize_google(audio)
		strip_txt=speak.strip()
		final_txt=strip_txt.split()
		print(final_txt)
	
		if 'place' in final_txt:
			for i in range(0,len(speak)):
				if final_txt[i]=='place':
					dir_name1=final_txt[i+1]
				if final_txt[i]=='directory':
					dir_name=final_txt[i+1]
					break
	
		new_place=dir_name+ '/' +dir_name1
	
		os.rename(dir_name1 , new_place)
	
	except:
		print("Could not understand your voice!!!")

