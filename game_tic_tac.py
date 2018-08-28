import random
board=[" " for i in range(9)]

def isBoardFull(board):

  # Return True if every space on the board has been taken. Otherwise return False.

    for i in range(1, 9):

        if board[i]==" ":
            return False

    return True
def player_victory(icon):
    
    
    if (board[0] == icon and board[1] == icon and board[2] == icon) or \
       (board[3] == icon and board[4] == icon and board[5] == icon) or \
       (board[6] == icon and board[7] == icon and board[8] == icon) or \
       (board[0] == icon and board[3] == icon and board[6] == icon) or \
       (board[1] == icon and board[4] == icon and board[7] == icon) or \
       (board[2] == icon and board[5] == icon and board[8] == icon) or \
       (board[0] == icon and board[4] == icon and board[8] == icon) or \
       (board[2] == icon and board[4] == icon and board[6] == icon):
        print("Player {} has won!".format(icon))
        print_board()
        return True
    elif "  " not in board:
        print("Its a draw!")
    else: return False
    
def print_board():
    row1="|{}|{}|{}|".format(board[0],board[1],board[2])
    row2="|{}|{}|{}|".format(board[3],board[4],board[5])
    row3="|{}|{}|{}|".format(board[6],board[7],board[8])

    print()
    print(row1)
    print(row2)
    print(row3)
    print()

def player_move(icon):
    
    if icon =="X":
        number=1
    elif icon=="O":
        number=2
    move=int(input("Enter your move(1-9): ").strip())
    if board[move-1]== " ":
        board[move-1]= icon
        
        if board[random.randint(1,8)]==" ":
            board[random.randint(1,8)]="O"
            print("Computer moves..")
        else:print("That space is taken..")
        
    else: print("That space is taken..")
    
icon=str(input("Choose a player (X/O): ")).upper().strip()


while not isBoardFull(board):
    
        print_board()
        player_move(icon)
        if player_victory("X"):
            break
        elif player_victory("O"):
            break
    
    
    

    
        
    
    
