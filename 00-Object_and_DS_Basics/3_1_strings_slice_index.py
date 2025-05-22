#python slice and indexing
mystring = "this is python jupyter"
print("string : ", mystring)                # this is python jupyter
print("string length ",len(mystring))            # 22

#Method 1: indexing
print("first letter of string ",mystring[0])     # t
print("last letter of string ",mystring[-1])      # r

print("syntax :  [start ,stop, step ]") #syntax #######################33
#Method 2: slicing
#string print  [start:stop:step]
print("first 4 letters of string ",mystring[::])  # this is python jupyter
#start
print("first 4 letters of string ",mystring[0:4])  # this
print("start after 2 letters of string ",mystring[2:])  # is is python jupyter
print("last 2 letters of string ",mystring[-2:])  # er
#stop
print("first 4 letters of string ",mystring[:4])    # this
print("last 4 letters of string ",mystring[:-4])    # this is python jup
#step - skipping letters
print("every second letter of string ",mystring[::2]) # ti spto uye
print("every thrid letter of string ",mystring[::3]) # tssyojyr
print("every fourth letter of string ",mystring[::4]) # t poue
#step with start &stop
print("every second letter of string ",mystring[1::2]) # hsi yhnjptr
print("every thrid letter of string ",mystring[1::3]) # h  tnut
print("every fourth letter of string range 1:20 ",mystring[1:20:4]) # hiynp
#reversing a string
print("reversed string ",mystring[::-1])          # retypuj nohtyp si siht