# Aufgabe 2: erforderliche Ausgabe:
#  123
# 1XOX
# 2 OO
# 3 X

def format_board(board):
    size = len(board)  # board size
    
    # Create the header row with column numbers
    header = ' ' + ''.join(str(i + 1) for i in range(size))
    
    # Build each row with row numbers and cell values
    rows = []
    for idx, row in enumerate(board):
        row_str = str(idx + 1) + ''.join(cell for cell in row)
        rows.append(row_str)
    
    # Combine header and rows with newlines
    return '\n'.join([header] + rows)

def assert_equal(actual, expected):
    if actual == expected:
        print("✅ Test Passed")
    else:
        print("❌ Test Failed")
        print("Expected:")
        print(expected)
        print("Actual:")
        print(actual)

board = [
    ['X', 'O', 'X'],
    ['O', ' ', ' '],
    [' ', 'X', 'O']
]

expected_output = ' 123\n1XOX\n2O  \n3 XO'

assert_equal(format_board(board), expected_output)


# Quelle: Chat GPT
