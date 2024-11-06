import random

class Hat:
  house = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

  @classmethod
  def sort(cls, name):
    print(name, "is in", random.choice(cls.house))
  
Hat.sort("Harry")