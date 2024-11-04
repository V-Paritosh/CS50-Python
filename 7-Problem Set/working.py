import re

def main():
  print(convert(input("Hours: ")))

def convert(s):
  match = re.fullmatch(r"(1[0-2]|0?[1-9]):?([0-5][0-9])? (AM|PM) to (1[0-2]|0?[1-9]):?([0-5][0-9])? (AM|PM)", s)
  if match:
    hour, minute, period, hour2, minute2, period2 = match.groups()
    
    hour = int(hour)
    hour2 = int(hour2) 
    if minute:
      minute = int(minute)
    else:
      minute = 0
    if minute2:
      minute2 = int(minute2)
    else:
      minute2 = 0

    time = convert_to_24(hour, minute, period)
    time2 = convert_to_24(hour2, minute2, period2)

    return f"{time} to {time2}"
  else:
    raise ValueError()

def convert_to_24(hour, minute, period):
  if period == "PM" and hour != 12:
      hour += 12
  elif period == "AM" and hour == 12:
      hour = 0
  return f"{hour:02}:{minute:02}"

if __name__ == "__main__":
  main()