#encoding in python 
#default UTF-8 code
#ascii needs to be in quote mark '' || "" because it is a string not to be used as a built-in character
#errors (strict) will throw an error thus needs to be handled using except and try block

txt = "This string contains different characters Latin[ꬰ], Hindi[क], Chinese[市]."
print(txt.encode())
print(txt.encode(encoding='ascii', errors='backslashreplace'))
print(txt.encode(encoding='ascii', errors='ignore'))
print(txt.encode(encoding='ascii', errors='namereplace'))
print(txt.encode(encoding='ascii', errors='replace'))
print(txt.encode(encoding='ascii', errors='xmlcharrefreplace'))