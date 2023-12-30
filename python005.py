#operations on String (part1)
String1 = 'Hello World'
String2 = "Hello World Again"
print("\n")

#print the Strings
print("String1 = ", String1)
print("String2 = ", String2)
print("\n")

#length Operation
num1 = len(String1)
num2 = len(String2)
print("Length of String1 = ", num1)
print("Length of String2 = ", num2)
print("\n")

#index value of the String
print("String1[0] = ",String1[0])
print("String2[1] = ",String2[1])
print("String2[-2] = ",String2[-2])
print("\n")

"""We can generate the stream of strings using negative indices too.
"""

#calling the set of chars with the Index Value provided
print("String1[0:2] = ", String1[0:2])
print("String1[0:10] = ", String1[0:10])
print("String2[6:-1] = ", String2[6:-1])
print("String2[0:18] = ", String2[0:18])
print("String2[3:] = ", String2[3:])
print("String2[:] = ", String2[:])
print("String2[:-3] = ", String2[:-3])
print("\n")

#uppercase and lowercase
print("Uppercase of String1 = ", String1.upper())
print("Uppercase of String2 = ", String2.upper())
print("Lowercase of String1 = ", String1.lower())
print("Lowercase of String2 = ", String2.lower())
print("\n")

#multiline comment
String3 = """Multiline comment
Statement 1;
Statement 2;
Statement 3;
Statement 4;"""
print("String 3 is a (multiline) String.\n\n String3 = ", String3)
print("\n")

#loop in string
for i in String1:
    print(i, end=" ")
print("\n")

for i in String2:
    print(i, end=" ")
print("\n")

for i in String3:
    print(i, end=" ")
print("\n")