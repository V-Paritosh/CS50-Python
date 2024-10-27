import sys

try:
  print("hello, my name is", sys.argv[1])
except IndexError:
  print("Too few arguments")

#OR

if len(sys.argv) < 2:
  sys.exit("Too few arguments")

for arg in sys.argv[1:]:
  print("hello, my name is", arg)


'''
sys.exit - exit the entire program
break - exit a function

1: - slices the list
1:-1 - rm the last vale and start at index 1
'''
