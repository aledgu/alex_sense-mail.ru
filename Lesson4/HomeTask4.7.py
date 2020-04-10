from functools import reduce

n = int(input('Введите число факториал которого хотите вычислить: '))

def fibo_gen():
    for i in range(1, n+1):
        if i < 16:
            yield i
factorial = reduce(lambda a, x: a*x, [int(a) for a in fibo_gen()])

print(factorial)