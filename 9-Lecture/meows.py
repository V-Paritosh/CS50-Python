#Constants
MEOWS = 3

for _ in range(MEOWS):
  print("meow")

class Cat:
  MEOWS = 3

  def meow(self):
    for _ in range(MEOWS):
      print("meow")

cat = Cat()
cat.meow()

#Type Hints, mypy, Docstring
def meow(n: int) -> str:
  """
  Meow n times.
  
  :param n: Number of times to meow
  :type n: int
  :raise TypeError: if n is not an int
  :return: A string of n meows, one per line
  :rtype: str
  """
  return "meow\n" * n

number: int = int(input("Number: "))
meows: str = meow(number)
print(meows, end="")

#argparse
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-n", default= 1, help="number of times to meow", type=int)
args = parser.parse_args()

for _ in range(args.n):
  print("meow")