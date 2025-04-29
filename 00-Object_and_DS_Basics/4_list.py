# Topic: list
list = [1, 2, 3, 4, 5]
list.append(6)
print('here is the list : ',list)
print('length of the list : ',len(list))

#Method 1 : list + format
print('here1 - format for list - {}'.format(list))
print('here2 - format for list - {0}{1}'.format(*list))
print('here3 - format for list - {0}{1}'.format(list[0],list[1]))
print('here4 - format for list - {0}'.format(list[0]))

#Method 2 : list + ARRAY
from array import array
arr = array('i',list)
print('\nhere - format for list - {}\n'.format(arr))

#Method 3 : list + LIST ,append,pop
newlist = ['three','four']
anotherlist = list + newlist
print('here - format for ADDED list - {}'.format(anotherlist))
anotherlist.append('five')                                              #added to the end of the list
print('here - format for ADD-on list - {}'.format(anotherlist))
anotherlist[0] ='ONE'                                                   #first element replaced
print('here - format for pop-on list - {}'.format(anotherlist))
anotherlist.pop()                                                       #last element deleteled by default pop(-1)
anotherlist.pop(3)                                                      #third element deleted
print('here - format for pop-on list - {}'.format(anotherlist))         

#Method 4 : list + sort
#anotherlist.sort()                                                     #sorts the list
#print('here - format for sort-on list - {}'.format(anotherlist))
# above statment won't work : TypeError: '<' not supported between instances of 'int' and 'str'

#Method 4 : list + sort
list_1 = ['one','two','three','four','five']
list_1.sort()                                                     #sorts the list
print('here - format for sort-on list - {}'.format(list_1))

#Method 5 : list + reverse
anotherlist.reverse()                                                  #reverses the list
print('here - format for reverse-on list - {}'.format(anotherlist))


