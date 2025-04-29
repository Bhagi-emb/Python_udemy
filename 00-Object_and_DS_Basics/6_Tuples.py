#Tuples
# Will check how tuples & lists are different : tuples are immutable and lists are mutable

tuple1 = (1, 2, 3, 4, 5)
list1 = [1, 2, 3, 4, 5]

#print data
print("tuple1: ", tuple1)
print("list1: ", list1)

#check type
print("type of tuple1: ", type(tuple1))
print("type of list1: ", type(list1))

#check length
print("length of tuple1: ", len(tuple1))
print("length of list1: ", len(list1))

#update tuple1
#tuple1[0] = 10 # this will give an error as tuples are immutable
#update list1
list1[0] = 10 # this will not give an error as lists are mutable

#check data
print("tuple1: ", tuple1)
print("list1: ", list1)

#calling tuple1
print("tuple1[0]: ", tuple1[0])
print("tuple1[-1]: ", tuple1[-1])

#calling list1
print("list1[0]: ", list1[0])
print("list1[-1]: ", list1[-1])

#tuple functions
tuple1 = (1, 2, 1, 4, 1)
print("tuple1 count of 1: ", tuple1.count(1))
print("tuple1 index of 1: ", tuple1.index(1)) #first occurance
