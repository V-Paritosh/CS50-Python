def main():
  str = input("Input: ")
  print(rm_vowel(str))

def rm_vowel(str):
  for i in str:
    match i:
      case "a"|"e"|"i"|"o"|"u"|"A"|"E"|"I"|"O"|"U":
        str = str.replace(i, "")
      case _:
        str
  return str


main()