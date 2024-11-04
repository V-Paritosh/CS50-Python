def main():
  print(validate(input("IPv4 Address: ")))

def validate(ip):
  try:
    parts = ip.split(".")

    if len(parts) != 4:
      return False
    
    for part in parts:
      if int(part) < 0 or int(part) > 255:
        return False
  except ValueError:
    return False
  return True

if __name__ == "__main__":
  main()