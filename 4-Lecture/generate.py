import random

coin = random.choice(["heads", "tails"])
print(coin)

number = random.randint(0,10)
print(number)

cards = ["jack", "queen", "king",]
random.shuffle(cards)
for card in cards:
  print(card)

  

'''
To import a specific function from a library(module)
  - from random import choice
    coin = choice(["heads", "tails"])
    print(coin)
  
'''