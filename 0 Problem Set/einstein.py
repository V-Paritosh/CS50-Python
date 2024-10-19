def main():
  x = int(input("m: "))
  print("E:",calc(x))

def calc(mass):
  return mass*pow(300000000,2)

main()