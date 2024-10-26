def main ():
  grocery()
  
def grocery():
  food_li = {}
  while True:
    try:
      food = input("").upper()
      if food == "":
        break
      if food in food_li:
        food_li[food] += 1
      else:
        food_li[food] = 1

    except EOFError:
      break

  print_list(food_li)

def print_list(li):
  for food, amt in sorted(li.items()):
    print(f"{amt} {food}")
    
main()  