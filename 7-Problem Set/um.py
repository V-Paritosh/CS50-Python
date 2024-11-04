import re

def main():
  print(count(input("Text: ")))

def count(s):
  count = 0
  words = s.lower().split()
  for word in words:
    word = re.match(r"um[.,!?]*$", word)
    if word:
      count += 1
  return count

if __name__ == "__main__":
  main()