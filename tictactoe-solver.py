# Initialize board
board = [["-","-","-"],["-","-","-"],["-","-","-"]]
rows = range(3)
cols = range(3)

# Print the board
def print_board(board):
    print("\nPrinting board...")
    for row in rows:
        print(board[row])
    print("")

# Check if there is a winner
def check_for_winner(board):

    for row in rows:
        # Check if a row has all x's or all o's
        if board[row] == ["x","x","x"]:
            return "x won"
        if board[row] == ["o","o","o"]:
            return "o won"
        
        # Check if a column has all x's or all o's
        x_count = 0
        o_count = 0
        for col in cols:
            if board[row][col] == "x":
                x_count += 1
            if board[row][col] == "o":
                o_count += 1
        if x_count == 3:
            return "x won"
        if o_count == 3:
            return "o won"
    
    #Check if a diagonal has all x's or all o's
    x_count = 0
    o_count = 0
    for row in rows:
        for col in cols:
            if row == col:
                if board[row][col] == "x":
                    x_count += 1
                if board[row][col] == "o":
                    o_count += 1
    if x_count == 3:
        return "x won"
    if o_count == 3:
        return "o won"
    x_count = 0
    o_count = 0
    for row in rows:
        for col in cols:
            if row + col == 2:
                if board[row][col] == "x":
                    x_count += 1
                if board[row][col] == "o":
                    o_count += 1
    if x_count == 3:
        return "x won"
    if o_count == 3:
        return "o won"
    
    #Check if a draw
    filled_squares = 0
    for row in rows:
        for col in cols:
            if board[row][col] == "x" or board[row][col] == "o":
                filled_squares += 1
    if filled_squares == 9:
        return "draw"
    return "game ongoing"

# ###################################################
# #check_for_winner unit tests

# #game ongoing
# board = [["-","-","-"],["-","-","-"],["-","-","-"]]
# print_board(board)
# print(check_for_winner(board))

# #x won
# board = [["o","o","-"],["x","o","-"],["x","x","x"]]
# print_board(board)
# print(check_for_winner(board))

# #o won
# board = [["o","o","o"],["x","-","x"],["-","x","-"]]
# print_board(board)
# print(check_for_winner(board))

# #x won
# board = [["x","o","o"],["x","x","o"],["o","-","x"]]
# print_board(board)
# print(check_for_winner(board))

# #o won
# board = [["x","x","o"],["x","o","o"],["o","-","x"]]
# print_board(board)
# print(check_for_winner(board))

# #draw
# board = [["x","o","x"],["x","x","o"],["o","x","o"]]
# print_board(board)
# print(check_for_winner(board))
# ###################################################


# Check for legal moves
def move_is_legal(board,player,row,col):
    x_count = 0
    o_count = 0
    for row in rows:
        for col in cols:
            if board[row][col] == "x":
                x_count += 1
            if board[row][col] == "o":
                o_count += 1
    if x_count == o_count and player != "x":
        return False
    elif x_count > o_count and player != "o":
        return False
    elif x_count < o_count:
        return False
        
    
    if board[row][col] == "-":
        return True
    else:
        return False
    
###################################################
# move_is_legal unit tests

#x making a legal move
board = [["x","o","-"],["-","-","-"],["-","-","-"]]
player = "x"
row = 2
col = 1
print_board(board)
print("Player " + str(player) + " move in row " + str(row) + ", col " + str(col) +  " is legal: " + str(move_is_legal(board,player,row,col)))

#o making an illegal move
board = [["x","o","-"],["-","-","-"],["-","-","-"]]
player = "o"
row = 2
col = 1
print_board(board)
print("Player " + str(player) + " move in row " + str(row) + ", col " + str(col) +  " is legal: " + str(move_is_legal(board,player,row,col)))

#x making an illegal move
board = [["x","o","-"],["-","-","-"],["-","-","-"]]
player = "o"
row = 0
col = 0
print_board(board)
print("Player " + str(player) + " move in row " + str(row) + ", col " + str(col) +  " is legal: " + str(move_is_legal(board,player,row,col)))
###################################################
