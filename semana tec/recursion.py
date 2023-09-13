def factorial(n):
    if n == 0:
        return 1
    return (n * factorial(n-1))

def factorial_it(n):
    fact = 1
    for t in range(1, n+1):
        fact *= t
    print(fact)

# print("Este es el recursivo: ")
# print(factorial(998))
# print("Este es el iterativo: ")
# factorial_it(998)

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return (fib(n-1) + fib(n-2))

def fib_it(n):
    a = 0
    b = 1
    for t in range(n):
        a, b = b, a + b
    return a

print("Este es el recursivo: ")
print(fib(50))
print("Este es el iterativo: ")
print(fib_it(50))