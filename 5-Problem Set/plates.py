def main():
  plate = input("Plate: ")
  if is_valid(plate):
    print("Valid")
  else:
    print("Invalid")


def is_valid(s): 
  return is_len_valid(s) and start_letter(s) and no_psp(s) and end_num(s)

def is_len_valid(s):
  return 2 <= len(s) <= 6

def start_letter(s):
  for i in range(2):
    if s[i].isalpha():
      continue
    else:
      return False
  return True
    
def no_psp(s):
  for i in s:
    if not i.isalnum():
      return False
  return True

def end_num(s):
  num_start = False
  for i in range(len(s)):
    if s[i].isdigit():
      if not num_start:
        if s[i] == '0':
          return False
        num_start = True
    elif num_start and not s[i].isdigit():
      return False
  return True  

if __name__ == "__main__":
  main()