import csv
from tabulate import tabulate
from pyfiglet import Figlet
figlet = Figlet()

def main():
  figlet.setFont(font="big")
  print(figlet.renderText("Password Manager"))

  while True:
    print("1) Add a new Password\n" +
          "2) Delete a Password\n" +
          "3) Update a Password\n" +
          "4) Display All Passwords\n" +
          "5) Exit")
    option = input("Input: ")
    match option:
      case "1":
        print("\nAdd a password")
        account = input("Account: ")
        username = input("Username/email: ")
        password = input("Password: ")
        print("\n",add_password(account, username, password),"\n")
      case "2":
        print("\nDelete a password")
        account = input("Account: ")
        print("\n",delete_password(account),"\n")
      case "3":
        print("\nUpdate a password")
        account = input("Account: ")
        new_password = input("New Password: ")
        print("\n",update_password(account, new_password),"\n")
      case "4":
        print("\n",display(),"\n")
      case "5":
        print("\nExiting Password Manager.")
        break
      case _:
        print("\nWrong Input. Please try again.\n")

def add_password(account, username, password):
  csv_file = False
  try:
    with open("password.csv", "r", newline="") as file:
      reader = csv.reader(file)
      if not any(reader):
        csv_file = True
      else:
        file.seek(0)
        header = next(reader)
        if header != ["Account", "Username/email", "Password"]:
          csv_file = True
  except FileNotFoundError:
    csv_file = True
  
  if csv_file:
    with open("password.csv", "w", newline="") as file:
      fieldnames = ["Account", "Username/email", "Password"]
      writer = csv.DictWriter(file, fieldnames=fieldnames)
      writer.writeheader()
      writer.writerow({"Account": account, "Username/email": username, "Password": password})
  else:
    with open("password.csv", "a", newline="") as file:
      writer = csv.writer(file)
      writer.writerow([account, username, password])

  return f"Password: {password} for Account: {account} has been added."

def delete_password(account):
  rows = []
  account_found = False
  try:
    with open("password.csv", "r", newline="") as file:
      reader = csv.DictReader(file)
      for row in reader:
        if (row["Account"] == account.strip()):
          account_found = True
        else:
          rows.append(row)
  except FileNotFoundError:
    return "No passwords stored"
  
  if account_found:
    with open("password.csv", "w", newline="") as file:
      fieldnames=["Account", "Username/email", "Password"]
      writer = csv.DictWriter(file, fieldnames=fieldnames)
      writer.writeheader()
      writer.writerows(rows)
    return f"Password for '{account}' has been deleted."
  else:
    return f"No password found for '{account}'."

def update_password(account, new_password):
  rows = []
  account_found = False
  try:
    with open("password.csv", "r", newline="") as file:
      reader = csv.DictReader(file)
      for row in reader:
        if (row["Account"] == account.strip()):
          row["Password"] = new_password
          account_found = True
        rows.append(row)
  except FileNotFoundError:
    return "No passwords stored yet."

  if account_found:
    with open("password.csv", "w", newline="") as file:
      fieldnames=["Account", "Username/email", "Password"]
      writer = csv.DictWriter(file, fieldnames=fieldnames)
      writer.writeheader()
      writer.writerows(rows)
    return f"Old Password has been updated to Password: {new_password} for Account: {account}."
  else:
    return f"No password found for '{account}'."
    
def display():
  try:
    with open("password.csv") as file:
      reader = csv.reader(file)
      rows = list(reader)
      if len(rows) <= 1:
        return "No passwords to display."
      header = rows[0]
      return (tabulate(rows[1:], headers=header, tablefmt="grid"))
  except FileNotFoundError:
    return "No passwords stored yet."

if __name__ == "__main__":
  main()