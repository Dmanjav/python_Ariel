import random

LadoA = ['Granjero','Maiz', 'Ganso', 'Zorro']
LadoB = []
Path = []

def estado_valido(L):
    if 'Ganso' in L and 'Maiz' in L and len(L) == 2:
        return False
    if 'Zorro' in L and 'Ganso' in L and len(L) == 2:
        return False
    return True

def reinicia_sistema():
    global LadoA, LadoB, Path
    LadoA = ['Granjero','Maiz', 'Ganso', 'Zorro']
    LadoB = []
    Path = []
    
def Trayecto(F, D):
    p1 = random.choice(F)
    if p1 != 'Granjero':
        F.remove(p1)
        D.append(p1)
    F.remove('Granjero')
    D.append('Granjero')
    return (p1, 'Granjero')
    
def HCR():
    F = LadoA
    D = LadoB
    intentos = 0
    while len(LadoB) != 4:
        intentos += 1
        p1, p2 = Trayecto(F, D)
        if estado_valido(F) and estado_valido(D):

            Path.append((p1,p2))
            F, D = D, F
        else:
            reinicia_sistema()
            F = LadoA
            D = LadoB
    return (Path)

def solucion_optima():
    path = HCR()
    while len(path) > 7:
        reinicia_sistema()
        path = HCR()
    return path


        
    
    
    
    
    