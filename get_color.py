from PIL import Image
from time import sleep

def get_color(color):
	if type(color) == int:
		return "none"
	if color[0] < 50 and color[1] < 50 and color[2] < 50:
		return "black"
	elif color[0] > 222 and color[1] > 222 and color[2] > 222:
		return "white"
	elif color[0] >= 128 and color[1] <= 128 and color[2] <= 128:
		return "red"
	elif color[0] <= 200 and color[1] >= 128 and color[2] <= 128:
		return "green"
	elif color[0] <= 128 and color[1] <= 200 and color[2] >= 128:
		return "blue"
	elif color[0] > 222 and color[1] > 222 and color[2] < 50:
		return "yellow"
	elif color[0] > 128 and color[1] < 128 and color[2] > 128:
		return "purple"
	else: 
		return "grey"
		
def get_img(dir):
	im = Image.open(dir)
	im = im.resize((1,1), Image.NEAREST)
	#print im.size #Get the width and hight of the image for iterating over
	pix = im.load()
	#print pix[0,0] #Get the RGBA Value of the a pixel of an image
	color = get_color(pix[0,0])
	del im
	return color

#z = get_img("C:\Users\Konstantin\Desktop\h\uu.jpg")
#print z
#                 R   G   B   A
#      black: 000 000 000 255
#         red: 255 000 000 255
#   orange: 255 128 000 255
#   yellow: 255 255 000 255
#    green: 000 255 000 255
#      blue: 000 000 255 255
#  purple: 128 000 128 255
#   white: 255 255 255 255
