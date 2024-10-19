def main():
  x = input("Enter:\n")
  print(convert(x)) 

def convert(str):
  if ":)" in str:
    str = str.replace(":)", "🙂")
  if ":(" in str:
    str = str.replace(":(", "🙁")

  return str

main()  