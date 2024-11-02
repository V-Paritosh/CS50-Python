import sys
import csv
from tabulate import tabulate

if len(sys.argv) < 2:
  sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
  sys.exit("Too many command-line arguments")
elif ".csv" not in sys.argv[1]:
  sys.exit("Not a CSV file")


try:
  with open(sys.argv[1]) as file:
    reader = csv.reader(file)
    count = 0
    rows = []
    for row in reader:
      if count == 0:
        header = row
        count += 1
      else:
        rows.append(row)
    print(tabulate(rows, headers=header, tablefmt="grid"))

except FileNotFoundError:
  sys.exit("File does not exist")