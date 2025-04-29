
# immutability - cannot change
print("immutability - cannot change")
name = "syam"
# name[0] = "Y"                                 # TypeError: 'str' object does not support item assignment
ch_name = name[1:]                              #Assign to new string    
print("before updating string : ",ch_name)      # yam
ch_name = 'p' + ch_name
print("after updating string : ",ch_name)       # pyam
print('\n')


# Example for string concat ( + *)
print("Example for string concat ( + *)")
str1 = "Hello"
str2 = "World"
print("str1 : ",str1)                          # Hello
print("str2 : ",str2)                          # World
str1 = str1 + " " + str2                        #adding space between two strings
print(str1)                                     # Hello World
print("\n")

# Example for string repeat
print("Example for string repeat : multiplication")
str = "z"
str = str * 10                                #repeat string
print(str)                                     # zzzzzzzzzz
print('\n')

# Example for number concat 
print("Example for number concat")
num1 = 10
num2 = 20
num3 = num1 + num2
print("num add : ",num3)                        # 30
 
num1 = '10'
num2 = '20'
num3 = num1 + num2
print("num as str add: ",num3)                 # 1020
