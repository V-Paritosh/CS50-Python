def main():
  order()

def order():
  item_li = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
  }
  cost = 0
  while True:
    try:
      item = input("Item: ").title()
      for k in item_li:
        if k == item:
          cost += item_li[k]
          print("Cost: $", format(cost, ".2f"), sep="")
    except EOFError:
      break
  
main()