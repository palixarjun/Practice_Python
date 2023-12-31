#string operations in the python

#capitalize()
txt = "this is an un-capitalized string."
print(txt)
print(txt.capitalize())
print('\n')

#casefold()
txt2 = "This Is a Capitalized String."
print(txt2)
print(txt2.casefold())
print('\n')

#center()
txt3 = "String"
print(txt3.center(8))
print(txt3.center(8, '0'))
print(txt3.center(8, '\n'))
print('\n')

#count()
txt4 = 'aabbccddeeff'
print("txt4.count('a') = ", txt4.count('a'))
print('\n')

#endswith()
txt5 = 'string5'
print("txt5.endswith('5') = ", txt5.endswith('5'))
print()

#find() and index()
#find() will return (-1) value if the character || string is not found
#index() will return error if the character || string is not found
txt6 = "String5"
print("txt6.find('5') =",  txt6.find('5'))
print("txt6.find('6') =", txt6.find('6'))
print("txt6.index('5') =", txt6.index('5'))
print()

#expandtabs(tabsize)
txt7 = "a\tr\tj\tu\tn"
print(txt7)
print(txt7.expandtabs())
print(txt7.expandtabs(2))
print(txt7.expandtabs(4))
print(txt7.expandtabs(8))
print(txt7.expandtabs(10))
print()