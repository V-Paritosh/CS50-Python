def main():
  str = input("Input: ")
  print(shorten(str))

def shorten(str):
  for i in str:
    match i:
      case "a"|"e"|"i"|"o"|"u"|"A"|"E"|"I"|"O"|"U":
        str = str.replace(i, "")
      case _:
        str
  return str

if __name__ == "__main__":
  main()