#python program on various list operations

#defining a list
mylist = [10,20,30,40,50,60,70,80,90,100]

#printing mylist
print('mylist = ', mylist)

#length of the list
print('length of the mylist =', len(mylist))

#printing the type of <list>
print(type(mylist))

#constructing a list
mylist_2 = list(('apple', 'mango', 'banana', 'sapodilla'))
print('mylist_2 = ' ,mylist_2)

#accessing the items in string
print('accessing the elements in the string')
for i in range((len(mylist) - 1)):
    print(('mylist[{}] = {}').format(i, mylist[i]))
    