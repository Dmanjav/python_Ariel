from math import sqrt
from turtle import fd, rt, done, circle

#PHI = 1 / ((sqrt(5) - 1) / 2 )
PHI = 2 / (sqrt(5) -1)

def square():
    for _ in range(4):
        fd(50)
        rt(90)
          
# square()
# circle(50, 120)
# done()

def spiral(n):
    x = 4
    for _ in range(n):
        circle(x, 90)
        x *= PHI
        
# spiral(9)
# done()

def print_fibonacci(n):
    a, b = 1, 1
    for _ in range(n):
        c = b / a
        print(f'{a:15d}{b:15d}{c:20.15f}')
        a, b = b, a + b
        
print_fibonacci(50)