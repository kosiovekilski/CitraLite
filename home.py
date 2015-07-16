import os

thumbnail = str(os.getcwd())

def get_letter(letter):
    case = {
        'C': "\\files\\C.png",
		'H': "\\files\\H.png",
		'I': "\\files\\I.png",
		'L': "\\files\\L.png",
		'O': "\\files\\O.png",
		'T': "\\files\\T.png",
		'U': "\\files\\U.png",
		'V': "\\files\\V.png",
		'X': "\\files\\X.png",
		'Y': "\\files\\Y.png",
	}
    return case.get(letter, "\\files\\thumbnail.png")
	
def home():
	if os.stat("DIRS.CitraLite").st_size != 0:
		f = open("index.html", "w")
		f.write("<html><head><title>CitraLite</title><link rel=\"stylesheet\" type=\"text/css\" href=\"files\style.css\"></head><body><center><img src=\"files\logo.png\" width=\"800px\" /><br><a href=\"colors.html\"><button>ColorSort</button></a><div>")
		with open('DIRS.CitraLite') as dirs:
			for dir in dirs:
				dir = dir.replace("\n", "")
				f.write("<div id=\"cli\"><a href=\"")
				f.write(str(dir.split("\\")[-1]))
				f.write(".html\"><img src=\"\\")
				a = thumbnail + "\\" + dir.split("\\")[-1] + ".png"
				print a
				if  os.path.isfile(thumbnail + "\\" + dir.split("\\")[-1] + ".png") == True:
					f.write(str(thumbnail + "\\" + dir.split("\\")[-1] + ".png"))
				else:
					letter = dir.split("\\")[-1][0]
					f.write(str(thumbnail))
					f.write(str(get_letter(letter.upper())))
				f.write("\"/><p>")
				f.write(str(dir.split("\\")[-1] ))
				f.write("</p></a></div>")
		f.write("</div></body></html>")
		f.close()
