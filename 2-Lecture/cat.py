def main():
  number = get_number()
  meow(3)

def get_number():
  while True:
    n = int(input("What's n?"))
    if n > 0:
      return n
  
def meow(n):
  for _ in range(n):
    print("meow")

'''
i = 0
while i < 3:
  print("meow")
  i += 1

for i in [0 , 1 , 2]:
  print("meow")

Better version of For-Loop
- for i in range(3):
    print("meow")

Pythonic way to write a variable used for loops
- for _ in range(3):
    print("meow")

Truly Pythonic
- print("meow\n" * 3)

### EXAMPLE ASKING FOR USER INPUT AND USING THAT VALUE
while True:
  n = int(input("What's n?"))
  if n < 0:
    continue - Continue asking the user for input
  else:
    break - Exit the loop

for _ in range(n):
  print(meow)
###
'''
