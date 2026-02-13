#Excersice: Write a function to check if someone has won a game by placing 3 of the same pieces on one of the diagonal lines. 

def diagonal_winner(board):
    return (board[0][0] == board[1][1] == board[2][2] != ' ') or (board[2][0] == board[1][1] == board[0][2] != ' ')

    # if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
    #     return True
    # if board[2][0] == board[1][1] and board[1][1] == board[0][2]:
    #     return True
    # else:
    #     return False

assert_equal(
    diagonal_winner(
        [
            ['X', 'O', 'X'],
            ['X', 'X', 'O'],
            ['O', 'O', 'X']
        ]
    ),
    True
)

assert_equal(
    diagonal_winner(
        [
            ['X', 'X', 'O'],
            ['X', 'O', 'O'],
            ['O', 'X', 'X']
        ]
    ),
    True
)

assert_equal(
    diagonal_winner(
        [
            ['O', 'X', 'O'],
            ['X', 'X', 'X'],
            ['O', 'O', 'X']
        ]
    ),
    False
)


#Alternative Lösung
# def diagonal_winner(board):
#     middle = board[1][1]
#     return (
#             (middle == board[0][0] and middle == board[2][2]) or
#             (middle == board[0][2] and middle == board[2][0])
#     )