def a1():
    return 5
print("#1----------------------------")
print(a1())
print("#2----------------------------")
print(a1()+a1())

def a2():
    return 5
    return 10
print("#3----------------------------")
print(a2())

def a3():
    return 5
    print(10)
print("#4----------------------------")
print(a3())

def a4():
    print(5)

print("#5----------------------------")
x = a4()
print(x)

def a5(b,c):
    return(b+c)
print("#6----------------------------")
print((a5(4,6)+a5(1,4)))

def a6(b,c):
    return str(b) + str(c)
print("#7----------------------------")
print(a6(5,6))

def a7():
    b = 100
    print(b)
    if b>10:
        return 10
    else:
        return 5
    return 7
print("#8----------------------------")
print(a7())

def a8(b,c):
    if b>c:
        return 14
    else:
        return 7
    return 3
print("#9----------------------------")
print(a8(2,3))
print(a8(5,3))
print(a8(2,3) + a8(5,3))

def a9(b,c):
    return (b+c)
    return 10
print("#10----------------------------")
print(a9(3,4))

b=100
def a10():
    b = 300
    print(b)
print("#11----------------------------")
print(b)
a10()
print(b)

b=500
print(b)
def a11():
    b=300
    print(b)
    return b
print("#12----------------------------")
print(b)
a11()
print(b)

b=400
def a12():
    b = 500
    print(b)
    return b
print("#13----------------------------")
print(b)
y = a12()
print(y)


def a13():
    print(1)
    b()
    print(2)
def b():
    print(3)
print("#14----------------------------")
a13()

def a14():
    print(1)
    x = b2()
    print(x)
    return 10

def b2():
    print(3)
    return 5
print("#15----------------------------")
y = a14()
print(y)














