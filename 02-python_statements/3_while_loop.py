# WHILE LOOP
x = 0
while(x < 4) :
    #print("x value : ",x)
    print(f'x value {x}')
    x += 1
else :
    print(" x is greater tha 4")

#PASS -  Does noting pass it is used to avoid syntax error
x =[1,2,3]
for _ in x:
    pass   # without this pass it cause syntax error
print("PASS : end of lines")

#continue - goes to top of the closest enclosing loop
str ='hello'
for letter in str:
    if letter == 'h':
        continue
    print(f'CONTINUE : str : {letter}')

# break - breaks out of the closest enclosing loop
for letter in str:
    if letter =='o':
        break
    print(f'BREAK : str : {letter}')