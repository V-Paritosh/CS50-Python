import sys
from PIL import Image, ImageOps
from os.path import splitext

if len(sys.argv) < 3:
  sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
  sys.exit("Too many command-line arguments")

path1 = splitext(sys.argv[1])[1]
path2 = splitext(sys.argv[2])[1]

if path1 not in [".png", ".jpeg", ".jpg"]:
  sys.exit("Invalid input file extension")
if path2 not in [".png", ".jpeg", ".jpg"]:
  sys.exit("Invalid output file extension")

if path1 != path2:
  sys.exit("Input and output have different extensions")

try:
  shirt = Image.open("shirt.png")
  image = Image.open(sys.argv[1])
  image = ImageOps.fit(image, shirt.size)
  image.paste(shirt, shirt)
  image.save(sys.argv[2])

except FileNotFoundError:
  sys.exit("File does not exist")
