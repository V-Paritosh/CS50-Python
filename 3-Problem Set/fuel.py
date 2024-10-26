def main():
  e_f()

def fuel():
  while True:
    try:
      x,y = input("Fraction: ").split("/")
      percentage = int(x)/int(y)*100
      return (int(round(percentage)))
    except ValueError:
      pass  
    except ZeroDivisionError:
      pass
    
def e_f():
  x = fuel()
  if x <=1:
    return print("E")
  elif 100 >= x >=99:
    return print("F")
  elif x > 100:
    fuel()
  else:
    return print(x,"%", sep="")

main()