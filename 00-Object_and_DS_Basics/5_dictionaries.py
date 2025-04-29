#Dictinaries syntax : dict = {'key1' :'value1', 'key2' : 'value2'}
#Creating a dictionary
my_dict = {
    'name': 'John',
    'age': 30,
    'city': 'New York'
}

#Accessing values
print("Printing the dict:",my_dict)  # Output : {'name': 'John', 'age': 30, 'city': 'New York'}
print("name :",my_dict['name'])  # Output: John
print("age :",my_dict['age'])   # Output: 30
print("city :",my_dict['city'])  # Output: New York

#Adding a new key-value pair
my_dict['job'] = 'Engineer'
#Accessing the new value
print("Added entry - job :",my_dict['job'])   # Output: Engineer
#Updating an existing value
my_dict['age'] = 31
#Accessing the updated value
print("Updated age : ",my_dict['age'])   # Output: 31

#Removing a key-value pair
del my_dict['city']
#Accessing the removed value
#print(my_dict['city'])  # This will raise a KeyError
print("Removed entry - city :",my_dict.get('city'))  # Output: None
#printing the entire dictionary
print("Printing the updated dict",my_dict)  # Output: {'name': 'John', 'age': 31, 'job': 'Engineer'}

#Nested dictionaries
#Creating a nested dictionary
d = {'k1': 123 ,'k2':[0,1,2] ,'k3' : {'insidekey' :100}}
#printing the entire dictionary
print("New Dict",d)  # Output: {'k1': 123, 'k2': [0, 1, 2], 'k3': {'insidekey': 100}}
#Accessing nested dictionary
print("d['k3']['insidekey'] : ",d['k3']['insidekey']) # Output: 100
print("d['k2'][2]: ",d['k2'][2]) # Output: 100


#Dictionary methods
#Keys
print("print only keys",d.keys())  # Output: dict_keys(['k1', 'k2', 'k3'])
#Values
print("print only values",d.values())  # Output: dict_values([123, [0, 1, 2], {'insidekey': 100}])
#Items
print("print only Items",d.items())  # Output: dict_items([('k1', 123), ('k2', [0, 1, 2]), ('k3', {'insidekey': 100})])
#Checking if a key exists
print('k1' in d)  # Output: True

#Assigning a dictionary to other for particular key
list = {'key1' :['a','b','c','d']}
print("Printing the list",list)  # Output: {'key1': ['a', 'b', 'c', 'd']}
mylist = list['key1']
print("Printing the mylist",mylist)  # Output: ['a', 'b', 'c', 'd']
letter = mylist[2]
print("Printing the letter",letter)  # Output: c
#Dictionary comprehension
my_dict = {x: x**2 for x in range(5)}  #these include for loop
print("Dict with for loop :",my_dict)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
#upper case
letter.upper()
print("Printing the letter",letter)  # Output: c

##Other way 
list['key1'][2] = list['key1'][2].upper()
list['key2'] = 100
print("Printing the list",list)  # Output: {'key1': ['a', 'b', 'c', 'd']}
