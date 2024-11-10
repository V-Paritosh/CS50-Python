from project import add_password, delete_password, update_password, display
import csv

def test_save_data():
  global rows
  with open("password.csv", "r", newline="") as file:
    rows = []
    reader = csv.reader(file)
    for row in reader:
      rows.append(row)

def test_add_password():
  account = "test_account"
  username = "test_username"
  password = "test_password"
  assert add_password(account, username, password) == f"Password: {password} for Account: {account} has been added."

def test_delete_password():
  account = "test_account"
  username = "test_username"
  password = "test_password"
  add_password(account, username, password)
  assert delete_password(account) == f"Password for '{account}' has been deleted."

def test_delete_password_invalid():
  account = "nonexistent_account"
  assert delete_password(account) == f"No password found for '{account}'."

def test_update_password():
  account = "test_account"
  username = "test_username"
  old_password = "old_password"
  new_password = "new_password"
  add_password(account, username, old_password)
  assert update_password(account, new_password) == f"Old Password has been updated to Password: {new_password} for Account: '{account}'."

def test_update_password_invalid():
  account = "nonexistent_account"
  new_password = "new_password"
  assert update_password(account, new_password) == f"No password found for '{account}'."

def test_display_empty():
  with open ("password.csv", "w+") as file:
    file.truncate()
  assert display() == "No passwords to display."

def test_display():
  add_password("account", "username", "password")
  add_password("account1", "username1", "password1")
  result = display()
  assert "account" in result
  assert "username" in result
  assert "password" in result
  assert "account1" in result
  assert "username1" in result
  assert "password1" in result

def test_add_data():
  with open("password.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(rows)