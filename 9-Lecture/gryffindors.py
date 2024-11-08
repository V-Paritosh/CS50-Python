students = [
  {"name": "Hermione", "house": "Gryffindor"},
  {"name": "Harry", "house": "Gryffindor"},
  {"name": "Ron", "house": "Gryffindor"},
  {"name": "Draco", "house": "Slytherin"},
  {"name": "Padma", "house": "Ravenclaw"},
]

gryffindors = [
  student["name"] for student in students if student["house"] == "Gryffindor"
]

for gryffindor in sorted(gryffindors):
  print(gryffindor)

#Filter
def is_gryffindor(s):
  return s["house"] == "Gryffindor"

gryffindors_filter = filter(is_gryffindor, students)

for gryffindor in sorted(gryffindors_filter, key=lambda s: s["name"]):
  print(gryffindor["name"])

#Dictionary Comprehensions
students_dict = ["Hermione", "Harry", "Ron"]

gryffindors_dict = {student: "Gryffindor" for student in students_dict}
#[{"name": student, "house": "Gryffindor"} for student in students_dict]

print(gryffindors_dict)

#enumerate
students = ["Hermione", "Harry", "Ron"]

for i, student in enumerate(students):
  print(i + 1, student)