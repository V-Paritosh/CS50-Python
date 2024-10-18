#Ask user for their name
name = input("What's your name?\n").title().strip()

#Say hello to user
print("hello, " + name)

'''
Remove whitespace from str
- name = name.title().strip()
- name = name.strip()
- name = name.capitalize()

Concat
 - print("Hello,", name, " to CS50")
 - print("Hello, " + name + " to CS50")

Quotes in a print 
 - print("Hello, 'friend'")
 - print("Hello, \"friend\"")

F string
 - print(f"hello, {name}")

Multi line comment use """ text """
""" Hi """

'''