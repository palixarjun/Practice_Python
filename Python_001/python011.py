#Operation on the string

txt = " String with preceding & succeding white space characters. "
#length of string before stripping.
print("length = ", len(txt))
#strip() function
print("txt.strip() = ", txt.strip())
print("length after stripping = ", len(txt.strip()))
print("\n")

#seperating the string with special characters(' ', ',', etc.)
a = txt.strip().split(' ') #there were preceding and succeding white space characters.
print(a)
print('\n')

#concatenation of the strings
print('String 1'+'String 2')
print('String 1'+ ' '+'String 2')
print('\n')

#format operation on the string

txt1 = 'String string {} string string'
print(txt1.format(12))
print(('integers 1[{}] and other 2[{}]data type in between the string').format([12,122,223], 'String'))
