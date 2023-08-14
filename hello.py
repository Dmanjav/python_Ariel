import cmath

print("Hello World!")

def chicharronera(a, b, c):
    b_neg = b * - 1
    raiz = cmath.sqrt((b ** 2) - (4 * a * c))
    
    x1 = (b_neg + raiz) / 2
    x2 = (b_neg - raiz) / 2

    return x1, x2

print(chicharronera(5,4,2))