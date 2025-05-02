#FOR LOOP
# A for loop is used to iterate over a sequence (list, tuple, dictionary, set, or string) or other iterable objects.
# With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.
# The for loop does not require an indexing variable to set beforehand.

#SYNTAX:
# for item in iterable:
#     # do something with item
#     print(item)

#### for loop with list ####
print("for loop with list")
#Basic:
item =[1,2,3]
for it in item:
    print(it)
print("============")
for list in item:
    print(list)

#example 1: print even numbers 
print("for loop with list: example 1")
item = [1,2,3,4,5,6,7,8,9,10]
for list in item:    #print even number
    if list % 2 == 0:
        print("even number :" ,list)
    else:
        #print("odd number: ", list)
        print(f"odd number : {list}")

#example 2: add the sum
print("for loop with list: example 2")
add_sum = 0
for sum in item:
    add_sum = add_sum +sum
    print(f"sum of {sum} is {add_sum}") #white spaces shows its in loop 
print("============")
print(f"sum of all number is {add_sum}")

#### for loop with string ####
print("for loop with string")
#example 1: print each character
print("for loop with string: example 1")
str = "hello world"
for _ in str:
    print(_)

#### for loop with Tuples ####
print("for loop with Tuples")
#example 1: print each character
print("for loop with Tuples: example 1")
#tuples
tup =(1,2,3)    
i =0
for _ in tup:
    print("tup[",i,"] :",tup[i])
    i += 1

#example 2: tuple packing and unpacking
print("for loop with Tuples: example 2(packing and unpacking)")
tup = (1,2,3)
a,b,c = tup
print(a)

#example 3: tuple and list
print("for loop with Tuples: example 3(tuple and list)")
list = [(1,2,3),(4,5,6),(7,8,9)]
len(list)
for _ in list:
    print(_)
#tuple unpacking
print("Below example is tuple unpacking")
for (a,b,c) in list:
    print(a)
    print(b)
    print(c)

#example 4: unpacking tuple
print("for loop with Tuples: example 4(unpacking tuple)")
for a,b,c in list:  #without parenthesis
    print(a)
    print(b)
    print(c)

### for loop with dictionary ###
print("for loop with dictionary")
#example 1: print each keys
print("for loop with dictionary: example 1")
dict = {'k1':1,'k2':2,'k3':3}
for _ in dict:
    print(_) #print only keys

#example 2: print each values
print("for loop with dictionary: example 2")
print("=====items=======")
for _ in dict.items():
    print(_) #print key and value
print("=====key and value=======")
for k,v in dict.items():
    print(k)
    print(v)
print("=====value=======")
for _ in dict.values():
    print(_) #print only values