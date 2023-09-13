#
#Equipo: 
#Andrés Iván Rodríguez Méndez
#Diego Manjarrez Viveros
#Omar Polanco Bueno

import matplotlib.pyplot as plt

# def diccionarios():
#     telefonos = {'Luis': '555-333', 'Pedro': '444-222', 'Alexa': '123-456'}
#     print(telefonos)
#     print("Luis tiene telefono: ")
#     print(telefonos['Luis'])
    
#     telefonos['Cesar'] = '777-333'
#     print(telefonos)
    
#     if 'Cesar' in telefonos:
#         print("Cesar tiene telefono: ")
#         print(telefonos['Cesar'])
            
#     del telefonos['Pedro']
#     print(telefonos)
    
#     for key in telefonos:
#         print(key, ":", telefonos[key])
        
        
# diccionarios()

def leerTexto():
    palabras = {}
    with open("texto.txt", "r") as archivo:
        contendio = archivo.read()
        print(contendio)
        contendio = contendio.lower()
        contendio = contendio.replace("\n", " ")
        saltos = contendio.split(" ")
        for palabra in saltos:
            if palabra not in palabras and palabra != "":
                palabras[palabra] = 1
            elif palabra != "":
                palabras[palabra] += 1
    
    plt.bar(range(len(palabras)), list(palabras.values()), align='center')
    plt.xticks(range(len(palabras)), list(palabras.keys()), rotation=90)
    plt.show()
    print(palabras)
    print(len(palabras))
                    
def main():
    leerTexto()

main()