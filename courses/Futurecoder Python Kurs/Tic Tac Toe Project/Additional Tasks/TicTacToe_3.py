#Aufgabe 3

def format_board(board):
    first_row = ' '
    for i in range(len(board)):
        first_row += str(i + 1)
    joined_rows = [first_row]
    for i in range(len(board)):
        joined_row = str(i + 1) + ''.join(board[i])
        joined_rows.append(joined_row)
    return "\n".join(joined_rows)

def play_game():
    board = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' '],
    ]
    print(format_board(board))
    print('\nX to play:\n')
    play_move(board, 'X')
    print(format_board(board))
    print('\nO to play:\n')
    play_move(board, 'O')
    print(format_board(board))

def play_move(board, player):
    spalte = int(input()) #|
    reihe = int(input()) # -

    board[spalte - 1][reihe - 1] = player
    #-1, weil index fängt von 0 an

play_game()

#erforderliche Ausgabe: 
# <input: 2>
# <input: 1>
#  123
# 1
# 2X
# 3