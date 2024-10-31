names = []

with open("names.txt") as file:
  for line in file:
    names.append(line.rstrip())

for name in sorted(names):
  print(f"hello, {name}")

'''
Version 1
names = []

for _ in range(3):
  names.append(input("What's your name? "))

for name in sorted(names):
  print(f"hello, {name}")

Version 2
name = input("What's your name? ")

open("names.txt", "a")
file.write(f"{name}\n")
file.close()

Version 3
name = input("What's your name? ")

with open("names.txt", "a") as file:
  file.write(f"{name}\n")

Version 4
with open("names.txt", "r") as file:
  lines = file.readlines()

for line in lines:
  print("hello,",line.rstrip())

Version 5
with open("names.txt", "r") as file:
  for line in file:
    print("hello,",line.rstrip())

Version 6
'''