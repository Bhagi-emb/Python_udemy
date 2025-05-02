# **IF ELIF ELSE STATMENTS**
a = 10
b = 20

#If statement
if a>b:
    print("a is greater than b")
if a<b:
    print("a is less than b")

#If else statement
if a>b:
    print("a is greater than b")
else:
    print("a is less than b")

#If elif else statement
if a>b:
    print("a is greater than b")
elif a==b:
    print("a is equal to b")
else:
    print("a is less than b")

#example1:

hungry = True
if hungry:
    print("I am hungry")
else:
    print("I am not hungry")

#example2:
loc = "library"
if loc == "Auto Shop":
    print("Cars are cool!")
elif loc == "Bank":
    print("Money is cool!")
elif loc == 'library':
    print("Books are cool!")
elif loc == "Store":
    print("Welcome to the store!")
elif loc == "Home":
    print("Welcome home!")
else:
    print("Where are you?")
