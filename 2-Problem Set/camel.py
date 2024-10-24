def main():
  name = input("camelCase:\n")
  print(snake_case(name))

def snake_case(name):
  index_li = upp_index(name)
  org_name = name.lower()
  offset = 0
  for i in index_li:
    org_name = add_val_at_index(org_name, "_", i+offset)
    offset += 1
  return org_name

def upp_index(str):
  index_val = []
  index = 0
  for i in str:
    if i.isupper():
      index_val.append(index)
    index += 1
  return index_val

def add_val_at_index(org_str, value, index):
  new_str= org_str[:index] + value + org_str[index:]
  return new_str

main() 