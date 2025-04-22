#create text file - read and write in python
# open a file in write mode
#create text file - read and write in python
# open a file in write mode and write to it
try:
	with open("test.txt", "w") as file:
		file.write("Hello World\n")
		file.write("This is a test file.\n")
except IOError as e:
	print(f"An error occurred while writing the file: {e}")
try:
	with open("test.txt", "r") as file:
		contents = file.read()
		# print the contents of the file
		print(contents)
except IOError as e:
	print(f"An error occurred while reading the file: {e}")
try:
	with open("test.txt", "a") as file:
		file.write("This is an appended line.\n")
		# contents = file.read() #error because file is opened in append mode
		# print(contents)
except IOError as e:
	print(f"An error occurred while appending to the file: {e}")
	
try:
	with open("test.txt", "r") as file:
		contents = file.read()
		# print the contents of the file
		print(contents)
except IOError as e:
	print(f"An error occurred while reading the file: {e}")