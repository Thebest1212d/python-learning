# Aufgabe 1
def winner(board):
    if row_winner(board) == True or column_winner(board) == True or diagonal_winner(board) == True:
        return True
    else:
        return False
    

def winning_line(strings):
    piece = strings[0]
    if piece == ' ':
        return False
    for entry in strings:
        if piece != entry:
            return False
    return True

def row_winner(board):
    for row in board:
        if winning_line(row):
            return True
    return False


def column_winner(board):
    for col in range(len(board[0])):
        column = []
        for row in board:
            column.append(row[col])
        if winning_line(column):
            return True
    return False


def diagonal_winner(board):
    diagonal1 = []
    diagonal2 = []
    for i in range(len(board)):
        diagonal1.append(board[i][i])
        diagonal2.append(board[i][-i-1])
    return winning_line(diagonal1) or winning_line(diagonal2)

def format_board(board):
    lines = []
    joined_rows = []
    for row in board:
        joined_rows.append("|".join(row))
    for _ in board[0]:
        lines.append("-")

    line = f'\n{"+".join(lines)}\n'
    return line.join(joined_rows)


# #-------------------------------------------------------------------
# #TEST Code nur für Test die obigen Code (Line 1-52) 
# def check_winner(board):
#     def winning_line(strings):
#         piece = strings[0]
#         if piece == ' ':
#             return None
#         for entry in strings:
#             if piece != entry:
#                 return None
#         return piece

#     size = len(board)

#     # Check Rows
#     for row in board:
#         winner = winning_line(row)
#         if winner:
#             return winner

#     # Check Columns
#     for col in range(size):
#         column = [board[row][col] for row in range(size)]
#         winner = winning_line(column)
#         if winner:
#             return winner

#     # Check Diagonals
#     diagonal1 = [board[i][i] for i in range(size)]
#     diagonal2 = [board[i][size - i - 1] for i in range(size)]

#     winner = winning_line(diagonal1)
#     if winner:
#         return winner

#     winner = winning_line(diagonal2)
#     if winner:
#         return winner

#     return None 

# # Example Usage
# board = [
#     [' ', ' ', ' '],
#     ['X', 'X', 'O'],
#     ['O', 'O', 'X']
# ]

# result = check_winner(board)
# if result:
#     print(f"Winner is: {result}")
# else:
#     print("No winner yet.")
# #-------------------------------------------------------------------


# erforderliche Ausgabe:
#  | |
# -+-+-
# X|X|O
# -+-+-
# O|O|X