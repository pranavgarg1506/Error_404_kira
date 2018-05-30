def delete_folder:
	import os
	path=ask_path()
	os.system("espeak -v female3 'confirm to delete the folder'+path")
	confirm=ask_name()
	if (confirm=="yes") or (confirm=="ya") or (confirm=="yup") or (confirm=="sure"):
		os.system("rm -r "+path)
