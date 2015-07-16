#doesn't work
import os
from get_color import *

def color_html(dir, color):
	for dirname, dirnames, filenames in os.walk(dir):
		name = dirname.split("\\")[-1]
		f = open(color + "_CitraLite.html","w")
		f.write("<html><head><title>CitraLite - ")
		f.write(str(color))
		f.write("</title><link rel=\"stylesheet\" type=\"text/css\" href=\"files\style.css\"></head><body><center><img src=\"files\logo.png\" width=\"800px\" /><br><div>")		
		for filename in filenames:
			ex = filename.split(".")[-1] .lower()
			#print ex
			if ex == "jpg" or ex == "png":
				path = os.path.join(dirname, filename)
				gic = get_img(path)
				print gic
				if gic == color:
					print path
					f.write("<dic id=\"cli\"><img src=\"\\")
					f.write(str(path))
					f.write("\" width=\"100px\"/></div>")
		f.write("</div></html>")
		f.close()
		

color_html("C:\Users\Konstantin\Desktop", "black")

'''
def dir_html(dir):
	for dirname, dirnames, filenames in os.walk(dir):
		name = dirname.split("\\")[-1]
		print name
		f = open(name + ".html","w")
		f.write("<html><head><title>CitraLite - ")
		f.write(str(name))
		f.write("</title><link rel=\"stylesheet\" type=\"text/css\" href=\"files\style.css\"></head><center><a href=\"index.html\"><img src=\"files\logo.png\" width=\"50%\" /><br><div>")		
		for filename in filenames:
			ex = filename.split(".")[-1] .lower()
			if ex == "jpg" or ex == "png":
				path = os.path.join(dirname, filename)
				f.write("<img class=\"imgs\" src=\"\\")
				f.write(str(path))
				f.write("\"/>")
		f.write("/></div></html>")
		f.close()
		'''
