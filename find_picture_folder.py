import os, sys, getpass

def  find(dir):
	user = getpass.getuser()
	for dirname, dirnames, filenames in os.walk(dir):
		name = dirname.split('\\')[-1]
		dir_name = user + '\\'+ dirname.split("\\")[-1]
		if name == "Pictures" and dir_name in dirname:
			return dirname
	return "0"
	
def pic_dir():
	pic = find("D:\\")
	if pic == "0":
		pic = find("C:\\")
	return pic
