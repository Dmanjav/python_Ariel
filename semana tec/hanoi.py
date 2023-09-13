# def torres_de_hanoi(n, origen, destino, auxiliar):
#     if n == 1:
#         print(f"Mover el disco {n} desde torre {origen} a torre {destino}")
#         return
#     torres_de_hanoi(n - 1, origen, auxiliar, destino)
#     print(f"Mover el disco {n} desde la torre {origen} a la torre {destino}")
#     origen, auxiliar = auxiliar, origen
#     torres_de_hanoi(n-1, origen, destino, auxiliar)


# torres_de_hanoi(3, 'A', 'C', 'B')

def torres_de_hanoi2(n, A, C, B):
    if n > 0:
        torres_de_hanoi2(n - 1, A, B, C)
        print(f"Mover disco {n} desde torre {A} a torre {C}")
        torres_de_hanoi2(n - 1, B, C, A)


torres_de_hanoi2(3, 'A', 'C', 'B')