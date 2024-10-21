def main():
  x = input("Expression:\n")
  int1, sign, int2 = x.split(" ")
  interpreter(int1, sign, int2)


def interpreter(int1, sign, int2):
  num1 = float(int1)
  num2 = float(int2)
    
  if sign == "+":
    result = num1 + num2
  elif sign == "-":
    result = num1 - num2
  elif sign == "*":
    result = num1 * num2
  elif sign == "/":
    result = num1 / num2
  else:
    print("Unknown operation")
  print(result)

main()