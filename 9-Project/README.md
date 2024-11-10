# Password Manager

#### Video Demo: [URL](https://youtu.be/ljezCrUB2ug)

#### Description
A simple password manager that allows users to manage passwords for multiple accounts. It provides functions for adding, deleting, updating, and displaying passwords, all stored locally in a CSV file. The program runs continuously in a command-line interface until the user chooses to exit.

### Key Functions

1. **add_password(account, username, password)**
  - This function allows users to add new passwords for accounts. It begins by checking if the "password.csv" file exists using a try-except block. If the file does not exist or is empty, a boolean (`csv_file`) is set to `True`, indicating that the file needs to be created with appropriate headers. Otherwise, the program verifies that the file structure is correct by checking if the header matches the expected fields.
  - If `csv_file` is `True`, a new file is created using `csv.DictWriter`, which sets up headers: "Account," "Username/email," and "Password." The password information is then added to the CSV file. If `csv_file` is `False`, the program appends the new account data using `csv.writer`, ensuring only additions to the existing file. The function ends by confirming the addition of the password to the CSV file through a return message.

2. **delete_password(account)**
  - This function allows users to delete a specific account’s password. It uses `csv.DictReader` to read existing passwords, searching for the account name provided by the user. If it finds the account, a boolean (`account_found`) is set to `True`, and the row is skipped in the new list, `rows`. Rows that do not match the specified account are added to `rows`, preserving all other account information.
  - After the loop, the function checks `account_found` to determine if the account was located. If `True`, `csv.DictWriter` overwrites "password.csv" with the updated `rows` list, excluding the deleted account. If `False`, it informs the user that the specified account does not exist. The function returns an appropriate message indicating success or failure of the deletion attempt.

3. **update_password(account, new_password)**
  - The update function is similar to the delete function but modifies an account’s password instead of removing it. Using `csv.DictReader`, the function searches for the account and updates the password if the account is found. If a match is located, `account_found` is set to `True`, and the row’s "Password" field is updated to `new_password`. The row is then added to the list `rows`, ensuring that updated information is saved.
  - After iterating through all rows, if `account_found` is `True`, `csv.DictWriter` updates "password.csv" with the revised list of rows. If no account matches, the function informs the user that no record exists for the specified account. The function returns an appropriate message indicating success or failure of the update attempt.

4. **display()**
  - The display function provides a neat, organized view of all saved passwords using the `tabulate` library for better readability. It opens "password.csv" and reads the file content with `csv.reader`, storing rows in the list `rows`. If `rows` contains only one entry (the header), it indicates that no passwords are stored. If there are multiple entries, the function returns the data in a table view using `tabulate`, which formats the data into a grid-style table with headers to improve the display of account information.
