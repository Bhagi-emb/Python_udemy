# example 1: print each character
mystr = 'sfgsfg'
mylist = []
for _ in mystr:
    mylist.append(_)
print("list of comp: ",mylist)

# (or next method)
mystr = 'sfgsfg'
mylist = [_ for _ in mystr]  # This is a list comprehension
print(mylist)

list= [x for x in "world"]
print("list of comp : ",list)

#example 2: print each character with  for loop condition
#range
mylist = [x for x in range(10)]
print("list of range : ", mylist)

#math operations
mylist = [x**2 for x in range(10)]
print("list of squares : ", mylist)

#if condition
mylist = [ x**2 for x in range (0,10) if x%2 ==0]
print("list of squares of even numbers : ", mylist)

# Tempeature conversion
celsius = [0, 10, 20.1, 34.5]
fahrenheit = [((float(9)/5)*temp + 32) for temp in celsius]
print("Celsius to Fahrenheit : \n ",celsius,"\n", fahrenheit)

# code explanation
fah = []
for temp in celsius:
    fah.append((float(9)/5)*temp + 32)
print("Celsius to Fahrenheit using for loop : \n ",celsius,"\n", fah)

#not recommended and simply way
res = [x if x%2 ==0 else 'oddnumber' for x in range(0,10)]
print("list of even numbers and odd numbers : \n", res)

# **Nested Loop - list comprehensions**
#nested list comprehension
list = []
for x in [1,5,2,3]:
    for y in [1,10,100]:
        list.append(x*y)
print("Nested list comprehension result : ", list)

mylist = [x*y for x in [1,2,3,4] for y in [10,20,30]]
print("Nested list comprehension with range : ", mylist)

mylist = [x*y for x in range(0,4) for y in range(10,40,10)]
print("Nested list comprehension with range : ", mylist)