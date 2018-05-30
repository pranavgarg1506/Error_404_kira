def hiding_dir():
	visible_dir=ask_name()
	hidden_dir="."+source_dir
	os.system('mv '+visible_dir+' '+hidden_dir)

