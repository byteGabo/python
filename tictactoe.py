from random import randrange

board = [['1', '2', '3'], ['4', 'X', '6'], ['7', '8', '9']]

def DisplayBoard (board):
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print('|   ' + board[0][0] +   '   |   ' + board[0][1] + '   |   ' + board[0][2] + '   |')
    print('|       |       |       |')
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print('|   ' + board[1][0] +   '   |   ' + board[1][1] + '   |   ' + board[1][2] + '   |')
    print('|       |       |       |')
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print('|   ' + board[2][0] +   '   |   ' + board[2][1] + '   |   ' + board[2][2] + '   |')
    print('|       |       |       |')
    print('+-------+-------+-------+')

    
def EnterMove(board):
    while True:
        move = int(input('Por favor escoja el numero de la casilla(1-9): '))
        if move < 1 or move > 9:
            print('Por favor ingrese un numero entre 1 y 9')
            continue
        elif str(move) not in board[0] and str(move) not in board[1] and str(move) not in board[2]:
            print('Lo siento, esa casilla ya esta tomada, por favor seleccione otra casilla')
            continue
        
        for row in range(0,3):
            for column in range(0,3):
                if board[row][column] == str(move):
                    board[row][column] = 'O'
        break

def MakeListOfFreeFields(board):
    free_square = []
    
    for row in range(0,3):
        for column in range(0,3):
            if board[row][column] == 'X' or board[row][column] == 'O':
                pass
            else:
                free_square.append(([row],[column]))
    
    print(free_square)
    
def VictoryFor(board, sign):
    pass    


DisplayBoard(board)
EnterMove(board)
DisplayBoard(board)
MakeListOfFreeFields(board)



