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
            if palabra not in palabras:
                palabras[palabra] = 1
            else:
                palabras[palabra] += 1
        
    del palabras[""]
    print(palabras)
    print(len(palabras))
                    
def main():
    leerTexto()

main()