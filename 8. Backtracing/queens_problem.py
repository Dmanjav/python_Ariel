from typing import Optional

Board = list[list[int]]

def solve(board: Board, col: int) -> Optional[Board]:
    if col == len(board):
        return board
    for row in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = True
            result: Optional[Board] = solve(board, col + 1)
            if result:
                return result
            board[row][col] = False
    
def is_safe(board: Board, row: int, col: int) -> bool:
    #Other queen on the left of the same row
    for i in range(col):
        if board[row][i]:
            return False
        
    #Other queen on the upper left diagonal
    for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        if board[i][j]:
            return False
    
    #Other queen on the lower left diagonal
    for i, j in zip(range(row + 1, len(board)), range(col - 1, -1, -1)):
        if board[i][j]:
            return False

    return True

def queens(n: int) -> Optional[Board]:
    board = [[False for _ in range(n)] for _ in range(n)]
    return solve(board, 0)

def print_solution(board: Board) -> None:
    for row in board:
        for x in row:
            if x:
                print('Q', end=' ')
            else:
                print('.', end=' ')
        print()

if __name__ == '__main__':
    board: Optional[Board] = queens(28)
    if board:
        print_solution(board)
    else:
        print('No solution found.')