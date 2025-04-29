# String Interpolation ->>> METHOD 1 <<<<--  .format()
# Syntax for string.format() :   'stringhere{} then also {}'.format('some1','some2')

print('here we fill :{}'.format('something'))
print("here , {} {} {} - .format()".format('this','the','new'))
print("here , {0} {2} {1} -.format()".format('this','the','new'))
print("here , {0} {1} {2} -.format()".format('this','the','new'))
print("here , {0} {0} {0} -.format()".format('this','the','new'))
print("here , {t} {th} {n} -.format()".format(t='this',th='the',n='new'))

### float formating follows "{value : width .precision f}"
result = 100/77
print("the result: -.format()",result)
print("the result is {r:0.3f} - .format()".format(r=result))
print("the result: {r:1.3f} -.format()".format(r=result))   #value:width(space before value).precision

# String Interpolation ->>> METHOD 2 <<<<--  f-string
# Syntax for f-string :   f'stringhere{variable} then also {variable}'
name = 'John'
age = 25
print(f'Using f-string -> Hello, {name}. You are {age} years old.')


# String Interpolation ->>> METHOD 3 <<<<--  % operator
# Syntax for % operator :   'stringhere % variable'
name = 'John'
age = 25
print('Using %% operator -> Hello, %s. You are %d years old.' % (name, age))  #print % by using %%


# String Interpolation ->>> METHOD 4 <<<<--  Template Strings
from string import Template
name = 'John'
age = 25
template = Template('Using template string -> Hello, $name. You are $age years old.')
print(template.substitute(name=name, age=age))


# String Interpolation ->>> METHOD 5 <<<<--  String Concatenation
name = 'John'
age = 25
print('Using string concat -> ''Hello, ' + name + '. You are ' + str(age) + ' years old.')


# String Interpolation ->>> METHOD 6 <<<<--  String Join
name = 'John'
age = 25
print(' Using string Join -> Hello, '.join([name, str(age)]))


# String Interpolation ->>> METHOD 7 <<<<--  String Literal
name = 'John'
age = 25
print('Using string concat -> ''Hello, {}'.format(name) + '. You are ' + str(age) + ' years old.')

