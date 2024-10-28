import emoji

str = input("Input: ")

if ":" in str:
  print("Output:", emoji.emojize(str, language="alias"))
else:
  print("Output:", str)

