# Initialize board
# board = [["-","-","-"],["-","-","-"],["-","-","-"]]
rows = range(3)
cols = range(3)

# Print the board
def print_board(board):
    for row in rows:
        print(board[row])
    print("")

# Check if there is a winner
def check_for_winner(board):
    #draw: return -1
    #game ongoing: return 0
    #x's won: return 1
    #o's won: return 2
    
    for row in rows:
        # Check if a row has all x's or all o's
        if board[row] == ["x","x","x"]:
            return 1
        if board[row] == ["o","o","o"]:
            return 2
        
    # Check if a column has all x's or all o's
    for col in cols:
        x_count = 0
        o_count = 0
        for row in rows:
            if board[row][col] == "x":
                x_count += 1
            if board[row][col] == "o":
                o_count += 1
        if x_count == 3:
            return 1
        if o_count == 3:
            return 2
    
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
        return 1
    if o_count == 3:
        return 2
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
        return 1
    if o_count == 3:
        return 2
    
    #Check if a draw
    filled_squares = 0
    for row in rows:
        for col in cols:
            if board[row][col] == "x" or board[row][col] == "o":
                filled_squares += 1
    if filled_squares == 9:
        return -1
    
    #game ongoing
    return 0

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
def move_is_legal(board,player,r,c):
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
        
    if board[r][c] == "-":
        return True
    else:
        return False
        

    
# ###################################################
# # move_is_legal unit tests

# #x making a legal move
# board = [["x","o","-"],["-","-","-"],["-","-","-"]]
# player = "x"
# row = 2
# col = 1
# print_board(board)
# print("Player " + str(player) + " move in row " + str(row) + ", col " + str(col) +  " is legal: " + str(move_is_legal(board,player,row,col)))

# #o making an illegal move
# board = [["x","o","-"],["-","-","-"],["-","-","-"]]
# player = "o"
# row = 2
# col = 1
# print_board(board)
# print("Player " + str(player) + " move in row " + str(row) + ", col " + str(col) +  " is legal: " + str(move_is_legal(board,player,row,col)))

# #x making an illegal move
# board = [["x","o","-"],["-","-","-"],["-","-","-"]]
# player = "o"
# row = 0
# col = 0
# print_board(board)
# print("Player " + str(player) + " move in row " + str(row) + ", col " + str(col) +  " is legal: " + str(move_is_legal(board,player,row,col)))
# ###################################################


# Find move score
def minimax(board,player):
    winner = check_for_winner(board)
    if winner == 1 and player == "x":
        return 1
    elif winner == 2 and player == "o":
        return -1
    elif winner == -1:
        return 0
    scores = []
    for row in rows:
        for col in cols:
            if player == "x":
                if move_is_legal(board,"o",row,col):
                    board[row][col] = "o"
                    scores.append(minimax(board,"o"))
                    board[row][col] = "-"
            elif player == "o":
                if move_is_legal(board,"x",row,col):
                    board[row][col] = "x"
                    scores.append(minimax(board,"x"))
                    board[row][col] = "-"
    if player == "o":
        return max(scores)
    elif player == "x":
        return min(scores)



# ###################################################
# # minimax unit tests
# player_to_move = "x" # draw
# board = [["-","-","-"],
#          ["-","-","-"],
#          ["-","-","-"]]

# player_to_move = "x" # draw
# board = [["x","o","o"],
#          ["o","x","x"],
#          ["x","-","o"]]

# player_to_move = "x" # o will always win
# board = [["x","o","x"],
#          ["-","o","o"],
#          ["-","-","x"]]


# player_to_move = "x" # x wins
# board = [["x","x","-"],
#          ["-","o","o"],
#          ["o","x","-"]]

# player_to_move = "x" # draw
# board = [["x","o","o"],
#          ["o","x","x"],
#          ["x","-","o"]]

# player_to_move = "o" # o wins
# board = [["x","-","-"],
#          ["-","o","-"],
#          ["o","x","x"]]

# player_to_move = "x" # x wins
# board = [["x","x","-"],
#          ["-","o","o"],
#          ["o","x","-"]]

# player_to_move = "o" # draw
# board = [["x","o","o"],
#          ["-","x","x"],
#          ["x","-","o"]]

# player_to_move = "o" # x can always win
# board = [["-","-","-"],
#          ["-","x","o"],
#          ["-","-","x"]]

player_to_move = "o" # draw
board = [["x","-","-"],
         ["-","-","-"],
         ["-","-","-"]]
# ###################################################


best_move = (-1,-1)
if player_to_move == "x":
    best_score = -100
if player_to_move == "o":
    best_score = 100
print("player to move: ", player_to_move)
print_board(board)
for row in rows:
    for col in cols:
        if move_is_legal(board,player_to_move,row,col):
            board[row][col] = player_to_move
            score = minimax(board,player_to_move)
            board[row][col] = "-"
            if player_to_move == "x":
                if score > best_score:
                    best_score = score
                    best_move = (row,col)
            elif player_to_move == "o":
                if score < best_score:
                    best_score = score
                    best_move = (row,col)

if best_score == -100 or best_score == 100:
    print("No valid moves!")
else:
    board[best_move[0]][best_move[1]] = player_to_move
    print("Best move:")
    print_board(board)
    print("best move: ", best_move)
    if best_score == -1:
        print("o wins")
    if best_score == 0:
        print("draw")
    if best_score == 1:
        print("x wins")

