import random

def main():
  lvl = get_lvl()
  guess(lvl)

def get_lvl():
  while True:
    try:
      lvl = int(input("Level: "))
      if lvl == 0:
        pass
      else:
        return lvl
    except ValueError:
      pass

def guess(lvl):
  guess_num = random.randint(1, lvl)
  print(guess_num)
  while True:
    try:
      guess_input = int(input("Guess: "))
      if guess_input < guess_num:
        print("Too small!")
        pass
      elif guess_input > guess_num:
        print("Too large!")
        pass
      else:
        return print("Just right!")
    except ValueError:
      pass

if __name__ == "__main__":
  main()