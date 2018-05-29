#!/usr/bin/python3

import speech_recognition as sr
import subprocess as su
import os

delete=['empty','remove','delete']


#get the audio from microphone
r = sr.Recognizer()
mic = sr.Microphone()


with mic as source:
	r.adjust_for_ambient_noise(source)
	print("PLz mention the path ")
	path_audio = r.listen(source)
		

def delete_files(dir_name):
		mydir=dir_name
		filelist = [ f for f in os.listdir(mydir)]
		for f in filelist:
    			os.remove(os.path.join(mydir, f))
		

try:
	input_data=r.recognize_google(path_audio)
	strip_path=input_data.strip()# removing extra spaces
	final_data=strip_path.split()#... splitting the data
	print(final_data)

#	def dict_check(final_data):
#		for i in range(0,len(input_data)):
#			for j in range(0,len(dictonary)):
#				if data[i]==dictonary[j]:
#					return dictonary[j][-1]
#					break 

	if 'remove' in final_data:
		for i in range(0,len(input_data)):
			if final_data[i]=='directory':
				dir_name=final_data[i+1]	
				break	
		
	delete_files(dir_name)
#	function=dict_check(final_data)

#	if function=='delete':
	#	delete_files(dir_name)
	
	
except:
	print("Could not understand")
	pass


















