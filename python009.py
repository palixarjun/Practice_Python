#basic datatypes in Python

"""
1. String 
2. integer
3. float 
4. complex
5. list
6. tuple
7. range 
8. dictionary
9. set
10. frozenset
11. bool
12. bytes
13. bytearray
14. memoryview
15. None
"""

x = str('String 1')
print(x)
print(type(x))
print("\n")

x = 123
print(x)
print(type(x))
print("\n")

x = float(12)
print(x)
print(type(x))
print("\n")

x = bool(0)
print(x)
print(type(x))
print("\n")

x = 1j
print(x)
print(type(x))
print("\n")


x = ['Apple', 'Mango', 'Banana']
print(x)
print(type(x))
print("\n")


x = {'Apple', 'Mango', 'Banana'}
print(x)
print(type(x))
print("\n")


x = ('Apple', 'Mango', 'Banana')
print(x)
print(type(x))
print("\n")

x = frozenset({'Apple', 'Mango', 'Banana'})
print(x)
print(type(x))
print("\n")

x = {0:'Apple', 1:'Mango', 2:'Banana'}
print(x)
print(type(x))
print("\n")

x = b'Hello'
print(x)
print(type(x))
print("\n")

x = bytearray(5)
print(x)
print(type(x))
print("\n")

x = memoryview(bytearray(5))
print(x)
print(type(x))
print("\n")

x = None
print(x)
print(type(x))
print("\n")