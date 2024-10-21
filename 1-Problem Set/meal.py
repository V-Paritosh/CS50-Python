def main():
  time = input("What time is it?\n")
  time = convert(time)
  meal(time)
  

def convert(time):
  hours, minutes = time.split(":")
  return float(hours) + float(minutes) / 60

def meal(time):
  if 7 <= time <= 8:
    print("breakfast time")
  elif 12 <= time <= 13:
    print("lunch time")
  elif 18 <= time <= 19:
    print("dinner time")  
  
if __name__ == "__main__":
  main()