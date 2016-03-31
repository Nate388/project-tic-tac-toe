theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 'mid-L': ' ', 'mid-M': ' ', 'mid-R':
' ', 'mid-R': ' ', 'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

def printBoard(board):
       print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
       print('-+-+-')
       print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
       print('-+-+-')
       print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
    # TO DO #################################################################
    # Write code in this function that prints the game board.               #
    # The code in this function should only print, the user should NOT      #
    # interact with this function in any way.                               #
    #                                                                       #
    # Hint: you can follow the same process that was done in the textbook.  #
    #########################################################################

def checkWinner(board, player):
       print('Checking if ' + player + ' is a winner...')
       if player == 'top-L' and player == 'top-M' and player == 'top-R': #horizontal
              return True
       elif player == 'mid-L' and player == 'mid-M' and player == 'mid-R':
              return True
       elif player == 'low-L' and player == 'low-M' and player == 'low-R':
              return True
       elif player == 'top-R' and player == 'mid-R' and player == 'low-R': #vertical 
              return True
       elif player == 'top-M' and player == 'mid-M' and player == 'low-M':
              return True
       elif player == 'top-L' and player == 'mid-L' and player == 'low-L':
              return True
       elif player == 'top-L' and player == 'mid-M' and player == 'low-R': #diagonal
              return True
       elif player == 'top-R' and player == 'mid-M' and player == 'low-L':
              return True
       elif player:
              return False
       
       



                           







    
    
    # TO DO #################################################################
    # Write code in this function that checks the tic-tac-toe board          #
    # to determine if the player stored in variable 'player' currently      #
    # has a winning position on the board.                                  #
    # This function should return True if the player specified in           #
    # variable 'player' has won. The function should return False           #
    # if the player in the variable 'player' has not won.                   #
    #########################################################################
    
    
def startGame(startingPlayer, board):
    # TO DO #################################################################
    # Add comments to each line in this function to describe what           #
    # is happening. You do not need to modify any of the Python code        #
    #########################################################################

    turn = startingPlayer #turn = the variable startingPlayer to store whatever information is in turn is also stored in startingPlayer
    for i in range(9): #setting up a for loop for the variable i in a range of 9
        printBoard(board) #calling the printBoard function to print the board
        print('Turn for ' + turn + '. Move on which space?') #printing to ask the current player what space they'd liek to move on
        move = input() # the variable move equals the current players input
        board[move] = turn # calling move to indicate whose turn it is and switch turns
        if( checkWinner(board, 'X') ): # checking the chechWinner function to see if X has filled the required spots on the baord to obtain a victory condition
            print('X wins!') #if so, player X has won
            break # break the loop and end
        elif ( checkWinner(board, 'O') ):# checking the chechWinner function to see if O has filled the required spots on the baord to obtain a victory condition 
            print('O wins!') # if so, O has won
            break # break the loop and end
    
        if turn == 'X': # if the turn was an X
            turn = 'O' # the next one is an O
        else: # if not
            turn = 'X' # then it's X's turn
        
    printBoard(board) # print the baord to see the results
    
