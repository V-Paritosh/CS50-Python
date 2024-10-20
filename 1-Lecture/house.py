name = input("What's your name?\n")

match name:
  case "Haryy" | "Hermione" | "Ron":
    print("Gryffindor")
  case "Draco":
    print("Slytherin")
  case _: #Works like else
    print("Who?")
