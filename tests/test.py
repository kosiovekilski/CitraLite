import os
import sys

if len(sys.argv) > 1:
	dir = str(sys.argv[1])
else:
	dir = "C:\\"

f = open("test.html", "w")
f.write("<html><head><style>img{height: 100px}html{background-color: black;}</style></head><img src=\"\\")
for dirname, dirnames, filenames in os.walk(dir):
  for filename in filenames:
	if filename.split(".")[-1] .lower() == "jpg":
		path = os.path.join(dirname, filename)
		f.write(str(path))
		f.write("\"/><img src=\"\\")

f.write("</html>")
f.close()
