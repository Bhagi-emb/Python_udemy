# ====================== RANGE =========================
#range(stop) -> range object
#range(start, stop[, step]) -> range object

print("====================== RANGE =========================")
print("only start 0-2")
for num in range(3):
    print(num)

print("start and stop and step(1,10,2)")
for num in range(1, 10, 2):
    print(num)

#range with length of list
print("range with length of list")
mylist =[1,2,3]
for num in range ( 0 ,len(mylist) ):
    print(mylist[num])

# list(range(0,10,2)) # [0, 2, 4, 6, 8]
# list(range(10, 0, -2)) # [10, 8, 6, 4, 2]
print("list(range(0,10,2))", list(range(0, 10, 2)))
print("list(range(10, 0, -2))", list(range(10, 0, -2)))
#range is a generator - means it does not create a list in memory

# **enumerate**
print("====================== ENUMERATE =========================")
index =0
for letter in'hello':
    print('at index {} the letter is {} '.format(index,letter))
    index += 1

for index in enumerate('hello'):
    print(index)   #this will print the index and the letter as a tuple

for index, letter in enumerate('hello'):
    print(index,'->' ,letter)  #this will print the index and the letter as a tuple

# ZIP FUNCTION
print("====================== ZIP =========================")

list3 = [1, 2, 3]
list4 = ['a', 'b', 'c']
lt = list(zip(list3, list4))
print(lt)
##Restart your kernel or Python session to clear the overwritten names.

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

#zip two list with for loop
for list in zip(list1, list2):
    print(list)  # prints each tuple (1, 'a'), (2, 'b'), (3, 'c')
    
#zip with enumerate
for index, (num, letter) in enumerate(zip(list1, list2)):
    print(index, '->', num, letter)  # prints index and the tuple elements

#CHECK in a List
print("====================== CHECK IN A LIST =========================")
print("'x' in [1,2,3,4] -> ", 'x' in [1, 2, 3, 4])  # False
print("'x' in ['x', 'y', 'z'] ->", 'x' in ['x', 'y', 'z'])  # True
print("'x' not in [1,2,3,4] -> ", 'x' not in [1, 2, 3, 4])  # True
print("'x' not in ['x', 'y', 'z'] ->", 'x' not in ['x', 'y', 'z'])  # False
# 'a' in 'a world' # true
print("'a' in 'a world' ->", 'a' in 'a world')  # True
# 'mykey' in {'mykey': 1, 'mykey2': 2} # True
print("'mykey' in {'mykey': 1, 'mykey2': 2} ->", 'mykey' in {'mykey': 1, 'mykey2': 2})  # True
dict = {'mykey': 1, 'mykey2': 2}
# 1 in dict.values() # true
# 1 in dict.keys() # false
print("1 in dict.values() ->", 1 in dict.values())  # True
print("1 in dict.keys() ->", 1 in dict.keys())  # False

# min and max of list
print("====================== MIN AND MAX =========================")
list = [1,10,30,100,5,20,3,4,5,6,7,8,9]
print("list ",list)
print("max(list) ->", max(list))  # 100
print("min(list) ->", min(list))  # 1
print("sum(list) ->", sum(list))  # 1000
print("sorted(list) ->", sorted(list))  # [1, 3, 4, 5, 5, 6, 7, 8, 9, 10, 20, 30, 100]
print("sorted(list, reverse=True) ->", sorted(list, reverse=True))  # [100, 30, 20, 10, 9, 8, 7, 6, 5, 5, 4, 3, 1]
# sorted(list, key=lambda x: x % 10)  # sorts by last digit
# print("sorted(list, key=lambda x: x % 10) ->", sorted(list, key=lambda x: x % 10))  # sorts by last digit
print("list.count(5) ->", list.count(5))  # 2
print("list.index(5) ->", list.index(5))  # 4 (first occurrence of 5)

# IMPORT LIBRARY
print("====================== IMPORT LIBRARY =========================")
import math
print("math.sqrt(16) ->", math.sqrt(16))  # 4.0
# every run results in different order
from random import shuffle
list = [3,4,2,6,7]
print("Original list:", list)
shuffle(list)
print("Shuffled list:", list)  # Randomly shuffled list

from random import choice
list = [1, 2, 3, 4, 5]
print("Random choice from list:", choice(list))  # Randomly selects one element from the list

from random import sample
list = [1, 2, 3, 4, 5]
print("Random sample of 3 from list:", sample(list, 3))  # Randomly selects 3 unique elements from the list

from random import randint
print("Random integer between 1 and 10:", randint(1, 10))  # Random integer between 1 and 10 (inclusive)

# **INPUT FROM TERMINAL**
print("====================== INPUT FROM TERMINAL =========================")
result = input("Press Enter to number...")  # Wait for user input 
print("input result:", result)  # Prints the input result
print("type of result :",type(result))  # Prints the type of the input result (always str)

# changing the input to int
result = int(result)
print("type of result :",type(result))  # Prints the type of the input result -> int
print("result + 10 ->", result + 10)  # Adds 10 to the input number