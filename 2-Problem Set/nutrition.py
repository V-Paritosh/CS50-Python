def main():
  input_fruit = input("Item: ").title()
  fruit_cal(input_fruit)

def fruit_cal(fruit):
  li_fruit = [
    {"name": "Apple", "cal": "130"},
    {"name": "Avocado", "cal": "50"},
    {"name": "Banana", "cal": "110"},
    {"name": "Cantaloupe", "cal": "50"},
    {"name": "Grapefruit", "cal": "60"},
    {"name": "Grapes", "cal": "90"},
    {"name": "Honeydew Melon", "cal": "50"},
    {"name": "Kiwifruit", "cal": "90"},
    {"name": "Lemon", "cal": "15"},
    {"name": "Lime", "cal": "20"},
    {"name": "Nectarine", "cal": "60"},
    {"name": "Orange", "cal": "80"},
    {"name": "Peach", "cal": "60"},
    {"name": "Pear", "cal": "100"},
    {"name": "Pineapple", "cal": "50"},
    {"name": "Plums", "cal": "70"},
    {"name": "Strawberries", "cal": "50"},
    {"name": "Sweet Cherries", "cal": "100"},
    {"name": "Tangerine", "cal": "50"},
    {"name": "Watermelon", "cal": "80"}
  ]
  for i in li_fruit:
    if i["name"] == fruit:
      print("Calories:",i["cal"])

main()