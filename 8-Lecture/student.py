class Student:
  def __init__(self, name, house, patronus):
    self.name = name
    self.house = house
    self.patronus = patronus

  def __str__(self):
    return f"{self.name} from {self.house}"
  
  @classmethod
  def get(cls):
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    return cls(name, house, patronus)
  
  #Getter
  @property
  def name(self):
    return self._name
  
  @property
  def house(self):
    return self._house
  
  #Setter
  @name.setter
  def name(self, name):
    if not name:
      raise ValueError("Missing name")
    self._name = name

  @house.setter
  def house(self, house):
    if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
      raise ValueError("Invalid house")
    self._house = house
  
  def charm(self):
    match self.patronus:
      case "Stag":
        return "🐴"
      case "Otter":
        return "🦦"
      case "Jack Russell terrier":
        return "🐶"
      case _:
        return "🪄"

def main():
  student = Student.get()
  print(student)
    
if __name__ == "__main__":
  main()

'''
() - Tuple: Immutable and similar to li
def main():
  student = get_student()
  print(f"{student[0]} from {student[1]}")

def get_student():
  name = input("Name: ")
  house = input("House: ")
  return (name, house)
'''