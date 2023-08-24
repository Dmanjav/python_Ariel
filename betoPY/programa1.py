def main():
    #list1 = [186, 699, 132, 272, 291, 331, 199, 1890, 788, 1601]
    #list1 = [160, 591, 114, 229, 230, 270, 128, 1657, 624, 1503]
    list1 = [15, 69.9, 6.5, 22.4, 28.4, 65.9, 19.4, 198.7, 38.8, 138.2]
    print(f"El promedio en la columna 1 es: {promedio(list1)}")
    print(f"La desviacion en la columna 1 es: {desviacion(list1, promedio(list1))}")
    
    
def promedio(list1):
    suma = 0
    for i in list1:
        suma += i
    promedio = suma / len(list1)
    return promedio

def desviacion(list1, promedio):
    suma = 0
    for i in list1:
        suma += ((i - promedio) ** 2)
    return (suma / (len(list1) - 1)) ** 0.5

main()