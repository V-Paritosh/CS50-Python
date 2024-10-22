students = [
  {"name": "Hermione", "house": "Gryfindor", "patronus": "Otter"},
  {"name": "Harry", "house": "Gryfindor", "patronus": "Stag"},
  {"name": "Ron", "house": "Gryfindor", "patronus": "Jack Russell terrier"},
  {"name": "Draco", "house": "Slytherin", "patronus": None}
]

for student in students:
  print(student["name"], student["house"], student["patronus"], sep=", ")

'''
students = ["Hermione", "Harry", "Ron"]

for student in students:
  print(student)

for i in range(len(students)):
  print(i+1, students[i])

{} - Dictionary
students = {
  "Hermione": "Gryffindor",
  "Harry": "Gryffindor",
  "Ron": "Gryffindor",
  "Draco": "Slytherin",
  }

for student in students:
  print(student, students[student], sep=", ")
'''