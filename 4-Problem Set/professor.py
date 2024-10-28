import random

def main():
  level = get_level()
  score = generate_integer(level)
  print(f"Score: {score}")

def get_level():
  while True:
    try:
      lvl = int(input("Level: "))
      if lvl == 1 or lvl == 2 or lvl == 3:
        return lvl
      else:
        pass
    except ValueError:
      pass

def generate_integer(level):
  count = 0
  score = 0
  if level == 1:
    min_val, max_val = 0, 9
  elif level == 2:
    min_val, max_val = 10, 99
  else:
    min_val, max_val = 100, 999
  while count < 10:
    x = random.randint(min_val, max_val)
    y = random.randint(min_val, max_val)
    answer = x + y

    attempts = 0
    while attempts < 3:
      try:
        user = int(input(f"{x} + {y} = "))
        if user == answer:
          score += 1
          break
        else:
          print("EEE")
          attempts += 1
      except ValueError:
        print("EEE")
        attempts += 1

    if attempts == 3:
      print(f"{x} + {y} = {answer}")
    count += 1
  return score


if __name__ == "__main__":
  main()
  