#program to find optimal move for a player
# X as maximizer and O as minimizer
#'_' is blank space on board
player, opponent ='x','o'

#to check no move is left and return True
def isMovesLeft(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
                return True
        return False

#if X win give value +1
#if O win give value -1
#if no one has won, so game results in a draw with value 0
def evaluate(b):
    #Checking for Rows for x or o victory
    for row in range(0,3):
        if(b[row][0] == b[row][1] and b[row][1] == b[row][2]):
            if(b[row][0] == player):
                return 1
            elif(b[row][0] == opponent):
                return -1
    #Checking for columns for x or o victory
    for column in range(0,3):
        if(b[0][column] == b[1][column] and b[1][column] == b[2][column]):
            if(b[0][column] == player):
                return 1
            elif(b[0][column] == opponent):
                return -1

    #Checking for diagonal for x or o victory
    if(b[0][0] == b[1][1] and b[1][1] == b[2][2]):
        if(b[0][0] == player):
            return 1
        elif(b[0][0] == opponent):
            return -1
    
    if(b[0][2] == b[1][1] and b[1][1] == b[2][0]):
        if(b[0][2] == player):
            return 1
        elif(b[0][2] == opponent):
            return -1
    #else if none of them won then return 0
    return 0


#minimax algorithm
def minimax(board, depth, isMax):
    score = evaluate(board)
    #if maximizer won the game return score
    if(score == 1):
        return score

    #if minimizer won the game return score
    if(score == -1):
        return score

    #if no move and winner return 0
    if(isMovesLeft(board) == False):
        return 0

    #if this maximizer's move
    if(isMax):
        best = -1000

        #traverse all cells
        for i in range(3):
            for j in range(3):
                #check if cell is empty
                if(board[i][j]=='_'):
                    #make a move
                    board[i][j] == player

                    # Call minimax recursively and choose
                    # the maximum value
                    best = max(best, minimax(board, depth+1, not isMax))

                    #undo the move
                    board[i][j] == '_'
        return best   
    
    else:
        best = 1000

        # Traverse all cell
        for i in range(3):
            for j in range(3):

                #check if cell is empty
                if(board[i][j]=='_'):
                    #make a move
                    board[i][j]==opponent

                    #call minimax recursively and choose
                    #the minimum value
                    best = min(best, minimax(board, depth+1, isMax))

                    #undo the move
                    board[i][j] = '_'
def findBestMove(board):
    bestVal = -1000
    bestMove = (-1, -1)

    #traverse all cells, evaluate minimax function for
    #all empty cells. and return the cell with optimal value
    for i in range(3):
        for j in range(3):

            #check if cell is empty
            if(board[i][j] == '_'):
                #make the move
                board[i][j] = player

                #compute evaluation funtion for this move
                moveVal = minimax(board, 0, False)

                #undo the move
                board[i][j] = '_'

                #if the value of the current move is more
                # than best value, then update best
                # 
                if(moveVal > bestVal):
                    bestMove = (i,j)
                    bestVal = moveVal

    print("The value of the best Move is :", bestVal)
    print()
    return bestMove

#drive code
board = [['x','o','x'],
         ['o','_','x'],
         ['_','_','x']]
bestMove = findBestMove(board)

print("The optimal move is :")
print("ROW:", bestMove[0], "COl:", bestMove[1])

