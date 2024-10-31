import inflect
p = inflect.engine()

def main():
  adieu()

def adieu():
  name_li = []
  while True:
    try:
      name = input("Name: ")
      if name == "":
        break
      name_li.append(name)
    except EOFError:
      print("Adieu, adieu, to", p.join(name_li))
      break

if __name__ == "__main__":
  main()