def main ():
  outdated()

def outdated():
  while True:
    try:
      date = input("Date: ")
      if date == "":
        break

      m, d, y = format_date(date)

      if d > 31 or m > 12:
        continue

      m, d = add_zero(m), add_zero(d)

      print(f"{y}-{m}-{d}")
      break
    except ValueError:
      print("pas")
      pass

def format_m(m):
  m_li = {
    "January": 1,
    "February": 2 ,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
  }

  for month, month_num in m_li.items():
    if m == month:
      return month_num
    
  return m

def format_date(date):
  if "/" in date:
    input_m, input_d, input_y = date.split("/")
    m, d, y = int(input_m), int(input_d), int(input_y)
  elif "," in date:
    input_month, input_d, input_y = date.replace(",", "").split()
    m = format_m(input_month)
    d, y = int(input_d), int(input_y)
  else:
    raise ValueError("df")
  
  return m, d, y

def add_zero(n):
  n = str(n)
  if len(n) == 1:
    n = "0" + n
    return n
  return n

main()  