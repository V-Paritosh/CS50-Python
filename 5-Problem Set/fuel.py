def main():
  while True:
    user = input("Fuel: ")
    try:
      gauge(user)
      break
    except ValueError:
      pass  
    except ZeroDivisionError:
      pass

def convert(fraction):
  x,y = fraction.split("/")
  x, y = int(x), int(y)
  if y == 0:
    raise ZeroDivisionError
  if x > y:
    raise ValueError
  percentage = int(x)/int(y)*100
  return int(round(percentage))
    
def gauge(percentage):
  if "/" in str(percentage):
    percentage = str(percentage)
    percentage = convert(percentage)
  if percentage <=1:
    return "E"
  elif 100 >= percentage >=99:
    return "F"
  elif percentage > 100:
    convert(percentage)
  else:
    return f"{percentage}%"

if __name__ == "__main__":
  main()