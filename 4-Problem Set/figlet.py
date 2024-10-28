from pyfiglet import Figlet
figlet = Figlet()
import sys
import random

ran = random.randint(0, 549)
figlet_li = figlet.getFonts()

if len(sys.argv) == 1:
  str = input("Input: ")
  figlet.setFont(font=figlet_li[ran])
  print(figlet.renderText(str))

elif len(sys.argv) == 3:
  if (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
    if sys.argv[2] in figlet_li:
      str = input("Input: ")
      figlet.setFont(font=sys.argv[2])
      print(figlet.renderText(str))
    else:
      sys.exit("Invalid usage")
  else:
    sys.exit("Invalid usage")
else:
  sys.exit("Invalid usage")
