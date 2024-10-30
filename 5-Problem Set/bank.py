def main():
  x = input("Greeting:\n")
  print(value(x))


def value(greeting):
  if greeting.lower().find("hello") >= 0:
    return 0
  elif greeting.lower()[0] == "h":
    return 20
  elif greeting.lower()[0] != "h":
    return 100

if __name__ == "__main__":
  main()
