#instance of the global and local variable in a function

myVariable1 = 'String1'

def MyFunction1():
    myVariable = 'String1'
    print("Value of myVariable1 = ", myVariable1)
    
print("myVariable1 = 'String1'")
print("Value of the myVariable1 (Before the function call)", myVariable1)
print("MyFunction1()")
MyFunction1()
print("Value of the myVariable1 (After the function call)", myVariable1)

myVariable2 = 'String2'
print("myVariable2 = 'String2'")
def MyFunction2():
    global myVariable2
    myVariable2 = 'String Changed'
    print("Value of myVariable2 = ", myVariable2)
    
print("Value of the myVariable2 (Before the function call)", myVariable2)
print("MyFunction2()")
MyFunction2()
print("Value of the myVariable1 (After the function call)", myVariable2)