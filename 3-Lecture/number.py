def main():
  x = get_int("What's x? ")
  print(f"x is {x}")

def get_int(prompt):
  while True:
    try:
      return int(input(prompt))
    except ValueError:
      pass #skip

main()

'''
Used to learn about ValueError
- Used "cat" as the input

Version 1
while True:
    try:
      x = int(input("What's x? "))
      break
    except ValueError:
      print("x is not an integer")
    
    'break like this or do like above
    else:
      break'

print(f"x is {x}")

'''