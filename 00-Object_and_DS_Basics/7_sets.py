#Sets - unordered collection of unique elements
#Sets are mutable - change the values
#Sets are unordered - no indexing
#Sets are iterable - can be looped through

myset = set()
print("type of myset: ",str(type(myset)))

#add elements
myset.add(1)
myset.add(2)
myset.add(3)
myset.add(1)
print("Updated myset: ", myset) #set will not allow duplicates

#remove elements
myset.remove(1)
print("Updated myset: ", myset)

set('Parallel')
print("set('Parallel'): ", set('Parallel')) #will remove duplicates



