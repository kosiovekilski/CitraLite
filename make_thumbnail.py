from PIL import Image
import os, sys

def make_th(dir):
	infile = "CitraLite"
	for dirname, dirnames, filenames in os.walk(dir):
		for filename in filenames:
			ex = filename.split(".")[-1] .lower()
			if ex == "jpg" or ex == "png":
				if dirname == dir:
					infile = os.path.join(dirname, filename)
					break
	#print infile
	if os.path.isfile(infile) == True:
		img = Image.open(infile)
		if img.size[0] >= img.size[1]:
			a = img.size[1]
		else:
			a = img.size[0]
		box = (0,0, a, a)
		area = img.crop(box)
		image = area.resize((200, 200), Image.ANTIALIAS)
		image.save(dir.split("\\")[-1] + ".png", 'jpeg')
		img.close()
		
make_th(str(sys.argv[1]))
