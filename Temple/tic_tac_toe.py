import random

print("Welcome to the game!")
print("---------------------")
board = [" ", " ", " ",
        " ", " ", " ",
        " ", " ", " "]
currentPlayer = "X"
winner = None
gameRunning = True


# game board
def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])


# take player input
def playerInput(board):
    run = True
    while run:
        inp = input("Please select a position to enter X between 1 to 9: ")
        try:
            inp = int(inp)
            if inp > 0 and inp < 10:
                if board[inp-1] == " ":
                    run = False
                    board[inp-1] = currentPlayer
                else:
                    print("Sorry, this space is already occupied!")
            else:
                print('Please type a number between 1 to 9!')
        except:
            print('Please type a number!')



# check for win or tie
def checkHorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != " ":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != " ":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != " ":
        winner = board[6]
        return True

def checkRow(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != " ":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != " ":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != " ":
        winner = board[3]
        return True


def checkDiag(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != " ":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[4] != " ":
        winner = board[2]
        return True


def checkIfWin(board):
    global gameRunning
    if checkHorizontal(board):
        printBoard(board)
        if winner == "X":
            print("You win!")
        elif winner == "O":
            print("The computer wins!")
        #print(f"The winner is {winner}!")
        gameRunning = False

    elif checkRow(board):
        printBoard(board)
        if winner == "X":
            print("You win!")
        elif winner == "O":
            print("The computer wins!")
        #print(f"The winner is {winner}!")
        gameRunning = False

    elif checkDiag(board):
        printBoard(board)
        if winner == "X":
            print("You win!")
        elif winner == "O":
            print("The computer wins!")
        #print(f"The winner is {winner}!")
        gameRunning = False

def checkIfDraw(board):
    global gameRunning
    if " " not in board and winner == None:
        printBoard(board)
        print("It is a draw!")
        gameRunning = False
    

# switch player
def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"

def computer(board):
    while currentPlayer == "O":
        position = random.randint(0, 8)
        if board[position] == " ":
            board[position] = "O"
            switchPlayer()
            print(f"Computer placed an O in position {position+1} ")

def main():
    while gameRunning:
        printBoard(board)
        playerInput(board)
        checkIfWin(board)
        checkIfDraw(board)
        switchPlayer()
        computer(board)
        checkIfWin(board)
        checkIfDraw(board)

choice = "y"
while choice == "y" or choice == "Y":
    board = [' ' for x in range(10)]
    main()
    choice = input("Do you want to play again? (y/n):")
    gameRunning = True
    