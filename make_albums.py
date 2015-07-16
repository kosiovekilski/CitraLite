import os

def dir_html(dir):
	for dirname, dirnames, filenames in os.walk(dir):
		name = dirname.split("\\")[-1]
		#print name
		f = open(name + ".html","w")
		f.write("<html><head><title>CitraLite - ")
		f.write(str(name))
		f.write("</title><link rel=\"stylesheet\" type=\"text/css\" href=\"files\style.css\"></head><center><a href=\"index.html\"><img src=\"files\logo.png\" width=\"800px\" /><br><div>")		
		for filename in filenames:
			ex = filename.split(".")[-1] .lower()
			if ex == "jpg" or ex == "png":
				path = os.path.join(dirname, filename)
				f.write("<div id=\"cli\"><img class=\"imgs\" src=\"\\")
				f.write(str(path))
				f.write("\"/></div>")
		f.write("/></div></html>")
		f.close()
