import sys
import csv

if len(sys.argv) < 3:
  sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
  sys.exit("Too many command-line arguments")
elif ".csv" not in sys.argv[1]:
  sys.exit("Not a CSV file")


try:
  with open(sys.argv[1]) as file:
    reader = csv.reader(file)
    count = 0

    with open(sys.argv[2], "w", newline="") as file2:
      fieldnames = ["first", "last", "house"]
      writer = csv.DictWriter(file2, fieldnames=fieldnames)
      writer.writeheader()
      
      for row in reader:
        if count == 0:
          count = 1
        else:
          name, house = row[0], row[1]
          last, first = name.split(", ")
          writer.writerow({"first": first.strip(), "last": last.strip(), "house": house.strip()})
except FileNotFoundError:
  sys.exit("File does not exist")