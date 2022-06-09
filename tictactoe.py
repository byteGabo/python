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
        elif move == 1:
            board[0][0] = 'O'
        elif move == 2:
            board[0][1] = 'O'
        elif move == 3:
            board[0][2] = 'O'
        elif move == 4:
            board[1][0] = 'O'
        elif move == 6:
            board[1][2] = 'O'
        elif move == 7:
            board[2][0] = 'O'
        elif move == 8:
            board[2][1] = 'O'
        elif move == 9:
            board[2][2] = 'O'
        
        break


DisplayBoard(board)
EnterMove(board)
DisplayBoard(board)



