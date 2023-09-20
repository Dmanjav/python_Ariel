import ProtoHCR
vector = ProtoHCR.solucion_optima()
cont = 1
vectorLadoA = ['Granjero', 'Zorro', 'Maiz', 'Ganso']
vectorLadoB = []
print('------------------------------')

print('INICIA EL JUEGO')
print('Lado A: ',vectorLadoA)
print('Lado B: ',vectorLadoB)
for i in vector:
    if cont % 2 != 0: #IDA
        print('------------------------------')
        print(f'El {i[0]} se va al Lado B con {i[1]}')
        if i[0] != i[1]:
            vectorLadoB.append(i[0])
            vectorLadoB.append(i[1])
        else:
            print(f'El {i[0]} se va al Lado B')
            vectorLadoB.append(i[0])
        
        if i[0] in vectorLadoA and i[1] in vectorLadoA:
            vectorLadoA.remove(i[0])
            vectorLadoA.remove(i[1])
        print('Lado A: ', vectorLadoA)
        print('Lado B: ', vectorLadoB)
        cont += 1
    else: #Vuelta
        print('------------------------------')
        
        if i[0] != i[1]:
            print(f'El {i[0]} se va al Lado A con {i[1]}')
            vectorLadoA.append(i[0])
            vectorLadoA.append(i[1])
        else:
            print(f'El {i[0]} se va al Lado A')
            vectorLadoA.append(i[0])
        if i[0] in vectorLadoB:
            vectorLadoB.remove(i[0])
            if i[1] in vectorLadoB:
                vectorLadoB.remove(i[1])
        print('Lado A: ', vectorLadoA)
        print('Lado B: ', vectorLadoB)
        
        cont += 1
    





