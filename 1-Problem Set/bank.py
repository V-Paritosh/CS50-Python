x = input("Greeting:\n").lower()

if x.find("hello") >= 0:
  print("$0")
elif x[0] == "h":
  print("$20")
elif x[0] != "h":
  print("$100")
