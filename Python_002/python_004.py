def star1():
    for i in range(6):
        for j in range(i):
            print('*', end='')
        print()

def star2():
    for i in range(5, 0, -1):
        for j in range(i):
            print('*', end='')
        print()

def star3():
    for i in range(5, 0, -1):
        for j in range(5-i):
            print(' ', end='')
        for k in range(i):
            print('*', end='')
        print()

def star4():
    for i in range(6):
        for j in range(6-i):
            print(' ', end='')
        for k in range(i):
            print('*', end='')
        print()

def star5():
    for i in range(5, 0, -1):
        for j in range(5-i):
            print(' ', end='')
        for k in range(i):
            print('*', end=' ')
        print()

def star6():
    for i in range(6):
        for j in range(5-i):
            print(' ', end='')
        for k in range(i):
            print('*', end=' ')
        print()

def star7(x):
    for i in range(x+1):
        for j in range(i):
            print('*', end='')
        print()
    for i in range(x-1, 0, -1):
        for j in range(i):
            print('*', end='')
        print()

















            
