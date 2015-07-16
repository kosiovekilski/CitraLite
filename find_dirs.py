import os
from find_picture_folder import *

def find_dirs(dir):
	if not os.path.isdir(dir):
		dir = pic_dir()
		
	fdirs = open("DIRS.CitraLite","w")
	last_dir = ""
	for dirname, dirnames, filenames in os.walk(dir):
	  for filename in filenames:
		ex = filename.split(".")[-1] .lower()
		if ex == "jpg" or ex == "png":
			if dirname != str(last_dir):
				fdirs.write(str(dirname) + '\n')
			last_dir = dirname
	fdirs.close()
