def main():
  x = int(input("What's x?\n"))
  if is_even(x):
    print("Even")
  else:
    print("Odd")

def is_even(n):
  return n % 2 == 0
  '''
  Pythonic (Specialty) - write a condition like a sentence 
  - return True if n == 0 else False
  '''
  
main()