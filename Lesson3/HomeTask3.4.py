def my_myfunc(x, y):
    return print(x**y)
my_myfunc(3, 2)

def my_func(x, y):
    b = x
    for i in range(y-1):
        x = x*b
    return print(x)
my_func(3, 2)