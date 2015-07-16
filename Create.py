from find_dirs import *
from home import *
#from make_thumbnail import *
from make_albums import *
import os
from color_html import *

dir = "C:\Users\Konstantin\Desktop"

find_dirs(dir)
print "find_dirs() ... fin"
with open('DIRS.CitraLite') as dirs:
	for dir in dirs:
		dir = dir.replace("\n", "")
#print dir
		if os.path.isdir(dir) == True:
	#		print "TRUE"
			os.system("make_thumbnail.py %s"%dir)
			dir_html(dir)
	#		print dir
		#	print os.path.isdir(dir)
print "make(), dir_html() ... fin"
home()
print "home() ... fin"
color_html(dir, "red")
print " red"
color_html(dir, "green")
print " green"
color_html(dir, "blue")
print " blue"
color_html(dir, "black")
print " black"
color_html(dir, "while")
print " while"
color_html(dir, "yellow")
print " yellow"
