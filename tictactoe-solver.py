# Initialize board
board = [["-","-","-"],["-","-","-"],["-","-","-"]]
rows = range(3)
cols = range(3)

# Print the board
def print_board(board):
    for row in rows:
        print(board[row])
    print("\n")

