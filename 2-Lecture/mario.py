def main():
  print_col(3)
  print_row(4)
  print_square(3)

def print_col(height):
  for _ in range(height):
    print("#")

def print_row(width):
  print("#" * width)

def print_square(size):
  for i in range(size): #For each row square
    for j in range(size): #For each brick in row
      print("#", end="")
    print()
  
  #OR
  print()
  for i in range(size):
    print("#" * size)

main()