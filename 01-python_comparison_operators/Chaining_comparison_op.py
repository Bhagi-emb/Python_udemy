# **Comparison ops and chaining comparison ops with logical**

##comparsion ops
a=5
b=3
print("a = ", a, " b= ", b)
print("a==b : ",a==b) #False
print("a!=b : ",a!=b) #True
print("a>b : ",a>b) #True
print("a<b : ",a<b) #False
print("a>=b : ",a>=b) #True
print("a<=b : ",a<=b) #False

##chaining comparison ops
a=3
b=5
c=7
print("a = ",a," b= ",b," c= ",c)
print("a<b<c : ",a<b<c) #True
print("a<b>c : ",a<b>c) #False
print("a<b and b<c : ",a<b and b<c) #True
print("a<b or b<c : ",a<b or b<c) #True
print("not(a<b<c) : ",not(a<b<c)) #False
print("not(a<b and b<c) : ",not(a<b and b<c)) #False