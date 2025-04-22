#create text file - read and write in python
# open a file in write mode and write to it
file = open("newtest.txt","w")
file.write("Hello World\n")
file.write("This is a test file.\n")
file.close()

# open a file in read mode and read from it
file = open("newtest.txt","r")
contents = file.read()
# print the contents of the file
print(contents)

# open a file in append mode and append to it
file = open("newtest.txt","a")
file.write("This a append data\n")

#print the contents of the file
file =open("newtest.txt","r")
contents = file.read()
print("Updated data:\n",contents)