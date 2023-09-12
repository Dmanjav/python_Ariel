import random

def numeros_random():
    for i in range(10):
        number = random.randint(1, 10)
        print(number, end= " ")
    
MIN = 1
MAX = 6

def tirar_dado():
    again = "y"
    
    while again.lower() == "y":
        print("Tirando el dado...")
        print("El valor es:")
        print(random.randint(MIN, MAX))
        print(random.randint(MIN, MAX))
        
        again = input("Tirar de nuevo? (y/n): ")

def moneda():
    caras = 0
    sol = 0
    for toss in range(100000):
        if random.randint(1, 2) == 1:
            #print("Cara")
            caras += 1
        else:
            sol += 1
            #print("Sol")
    
    print("Probabilidad de cara: ", caras/1000)
    print("Probabilidad de sol: ", sol/1000)

def main():
    #numeros_random()
    #tirar_dado()
    moneda()
    
if __name__ == "__main__":
    main()