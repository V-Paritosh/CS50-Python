import re

email = input("What's your email? ").strip()

if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):
  print("Valid")
else: 
  print("Invalid")

#r"^[^a-zA-Z0-9_]+@[^a-zA-Z0-9_]+\.edu$"


'''
EXPRESSION:
.   any character except a new line
*   0 or more repetitions
+   1 or more repetitions
?   0 or 1 repetition
{m} m repetitions
{m,n} m-n repetitions
^   matches the start of the string
$   matches the end of the string or just before the newline at the end of the string
[]    set of characters
[^]   complementing the set
\d    decimal digit
\D    not a decimal digit
\s    whitespace characters
\S    not a whitespace character
\w    word character, as well as numbers and the underscore
\W    not a word character
A|B     either A or B
(...)   a group
(?:...) non-capturing version

FLAGS:
re.IGNORECASE
re.MULTILINE
re.DOTALL
'''