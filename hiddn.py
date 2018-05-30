def hiding_dir():
	visible_dir=ask_name()
	hidden_dir="."+visible_dir
	os.system('mv '+visible_dir+' '+hidden_dir)

