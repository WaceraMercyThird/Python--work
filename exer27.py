# Memorizing Logic


x = 15
y = 4

# Output: x + y = 19
print('x + y =',x+y)

# Output: x - y = 11
print('x - y =',x-y)

# Output: x * y = 60
print('x * y =',x*y)

# Output: x / y = 3.75
print('x / y =',x/y)

# Output: x // y = 3
print('x // y =',x//y)

# Output: x ** y = 50625
print('x ** y =',x**y)


def num():
    x = 10
    y = 12

    # Output: x > y is False
    print('x > y is',x>y)

    # Output: x < y is True
    print('x < y is',x<y)

    # Output: x == y is False
    print('x == y is',x==y)

    # Output: x != y is True
    print('x != y is',x!=y)

    # Output: x >= y is False
    print('x >= y is',x>=y)

    # Output: x <= y is True
    print('x <= y is',x<=y)

    x = True
    y = False

    print('x and y is',x and y)

    print('x or y is',x or y)

    print('not x is',not x)

num()


def more_num():
    x1 = 5
    y1 = 5
    x2 = 'Hello'
    y2 = 'Hello'
    x3 = [1,2,3]
    y3 = [1,2,3]

    # Output: False
    print(x1 is not y1)

    # Output: True
    print(x2 is y2)

    # Output: False
    print(x3 is y3)

more_num()