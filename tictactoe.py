from random import randrange

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
    global free_square
    free_square = []
    
    for row in range(0,3):
        for column in range(0,3):
            if board[row][column] == 'X' or board[row][column] == 'O':
                pass
            else:
                free_square.append(([row],[column]))
    
    print(free_square)
    
def VictoryFor(board, sign):
    
    if sign == 'O':
        print('buscando si tu eres el ganador...')
    else:
        print('Buscando si la computadora gano el juego...')
       
    #FILAS
    if board[0][0] == sign and board[0][1] == sign and board[0][2] == sign:
            return True
    elif board[1][0] == sign and board[1][1] == sign and board[1][2] == sign:
            return True
    elif board[2][0] == sign and board[2][1] == sign and board[2][2] == sign:
            return True
            
    #COLUMNAS        
    elif board[0][0] == sign and board[1][0] == sign and board[2][0] == sign:
            return True
    elif board[0][1] == sign and board[1][1] == sign and board[2][1] == sign:
            return True
    elif board[0][2] == sign and board[1][2] == sign and board[2][2] == sign:
            return True
            
    #DIAGONALES        
    elif board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
            return True
    elif board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
            return True
    else:
        print('No hay un Ganador todavia, sigue jugando')
        
def DrawMove(board):
    while True:
        row = randrange(3)
        column = randrange(3)
        
        if ([row], [column]) not in free_square:
            continue
        else:
            board[row][column] = 'X'
            return

board = [['1', '2', '3'], ['4', 'X', '6'], ['7', '8', '9']]
numberOfMoves = 1
human = 'O'
computer = 'X'

print('Hola Bienvenido al juego tres en raya')
DisplayBoard(board)
print()

while numberOfMoves < 9:
    EnterMove(board)
    numberOfMoves += 1
    DisplayBoard(board)
    
    if VictoryFor(board, human) == True:
        print('Rompiste la computadora, tu eres una gran humano')
        break
    else:
        print('Aqui esta la lista de casillas vacias: ')
        MakeListOfFreeFields(board)
        print()
        DisplayBoard(board)
    
    print()
    print("es turno de la X")
    DrawMove(board)
    numberOfMoves += 1
    DisplayBoard(board)
    print()
    
    if VictoryFor(board, computer) == True:
        print('La computadora es mas inteligente que tu')
        break
    else:
        print('Aqui esta la lista de casillas vacias: ')
        MakeListOfFreeFields(board)
        print()
        DisplayBoard(board)
else:
    print('Es un EMPATE!')
    

print('??Gracias Por Jugar!')
    
    



