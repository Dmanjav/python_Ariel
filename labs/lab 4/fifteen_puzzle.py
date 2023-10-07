#----------------------------------------------------------
# Lab #4: A* Search Algorithm
# Solving the 15 puzzle.
#
# Date: 06-Oct-2023
# Authors:
#           A01747433 Carlos Alberto Sánchez Calderón
#           A01753486 Diego Manjarrez Viveros
#----------------------------------------------------------


from typing import Optional
from generic_search import astar, Node, node_to_path

Frame = tuple[tuple[int, ...], ...]


def solve_puzzle(frame: Frame) -> None:
    
    # The rest of the function's code goes here
    def goal_test(frame: Frame) -> bool:
        correctFrame: Frame = ((1, 2, 3, 4),
                    (5, 6, 7, 8),
                    (9, 10, 11, 12),
                    (13, 14, 15, 0))
        return correctFrame == frame
    
    def successors(frame: Frame) -> list[Frame]:
        posX: int = 0
        posY: int = 0
       
        
        frameTemp: list[Frame] = []
        for i in range(4):
            for j in range(4):
                if frame[i][j] == 0:
                    posX = j
                    posY = i
                    break
        
        if posY != 3:
            cpyFrame = list(frame)
            temp = [list(y) for y in cpyFrame]
            temp[posY][posX] =  temp[posY + 1][posX]
            temp[posY + 1][posX] = 0
            temp2 = [tuple(t) for t in temp]
            temp3 = Frame(temp2)
            frameTemp.append(temp3)

        if posY != 0:
            cpyFrame = list(frame)
            temp = [list(y) for y in cpyFrame]
            temp[posY][posX] =  temp[posY - 1][posX]
            temp[posY - 1][posX] = 0
            temp2 = [tuple(t) for t in temp]
            temp3 = Frame(temp2)
            frameTemp.append(temp3)

        if posX != 3:
            cpyFrame = list(frame)
            temp = [list(y) for y in cpyFrame]
            temp[posY][posX] =  temp[posY][posX + 1]
            temp[posY][posX + 1] = 0
            temp2 = [tuple(t) for t in temp]
            temp3 = Frame(temp2)
            frameTemp.append(temp3)

        if posX != 0:
            cpyFrame = list(frame)
            temp = [list(y) for y in cpyFrame]
            temp[posY][posX] =  temp[posY][posX - 1]
            temp[posY][posX - 1] = 0
            temp2 = [tuple(t) for t in temp]
            temp3 = Frame(temp2)
            frameTemp.append(temp3)
        return list(frameTemp)    
    
    def heuristic(frame: Frame) -> float:
        sum: float = 16
        correctFrame: Frame = ((1, 2, 3, 4),
                    (5, 6, 7, 8),
                    (9, 10, 11, 12),
                    (13, 14, 15, 0))
        for i in range(4):
            for j in range(4):
                if frame[i][j] == correctFrame[i][j]:
                    sum -= 1
        return sum
    
    
        

    resxult: Optional[Node[Frame]] = astar(frame, goal_test, successors, heuristic)
    if(resxult is None):
        print("nop")
    else:
        path: list[Frame] = node_to_path(resxult)
        xo: int = 0
        yo: int = 0

        xf: int = 0
        yf: int = 0
        value = 0
        if(len(path) == 2):
            print("Solution requires ", len(path) -1," step",sep="")
        else:
            print("Solution requires ", len(path) -1," steps",sep="")
        for f in range(len(path) - 1):
            for i in range(4):
                for j in range(4):
                    if path[f][i][j] == 0:
                        xo = j
                        yo = i
                        value = path[f+1][i][j]
                        
                    if path[f+1][i][j] == 0:
                        xf = j
                        yf = i
                   
            if yo < yf:
                print("Step ",f+1,": Move ", value,  " up",sep="")
            if yo > yf:
                print("Step ",f+1,": Move ", value,  " down",sep="")
            if xo < xf:
                print("Step ",f+1,": Move ", value,  " left",sep="")
            if xo > xf:
                print("Step ",f+1,": Move ", value,  " right",sep="")
  
def heuristic(frame: Frame) -> float:
        sum: float = 0
        correctFrame: Frame = ((1, 2, 3, 4),
                    (5, 6, 7, 8),
                    (9, 10, 11, 12),
                    (13, 14, 15, 0))
        for i in range(4):
            for j in range(4):
                if frame[i][j] == correctFrame[i][j]:
                    sum += 1
        return 16 - sum