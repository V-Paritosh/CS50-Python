from datetime import date
import re
import sys
import inflect

p = inflect.engine()

def main():
  birth = input("Date of Birth: ")
  try:
    birth = format_str(birth)
  except ValueError:
    sys.exit("Invalid Date")
  print(convert(birth))

def format_str(str):
  if re.search(r"^\d{4}-\d{2}-\d{2}$", str):
    return str
  else:
    raise ValueError
  
def convert(date_str):
  today_date = date.today()
  uy, um, ud = date_str.split("-")
  ty, tm, td = str(today_date).split("-")
  days = date(int(ty), int(tm), int(td)) - date(int(uy), int(um), int(ud))
  time = str(days * 24 * 60).split()
  return (p.number_to_words(time[0], andword="") + " minutes").capitalize()

if __name__ == "__main__":
  main()
