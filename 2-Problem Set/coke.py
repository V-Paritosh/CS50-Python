def main():
  amt = 50
  amount(amt)
  while True:
    n = int(input("Insert Coin: "))
    match n:
      case 25 | 10 | 5:
        if n < amt:
          amt -= n
          amount(amt)
        else:
          print("Change Owed:", n-amt)
          break
      case _:
        amount(amt)
        continue
    

def amount(n):
  print(f"Amount Due: {n}")

main()