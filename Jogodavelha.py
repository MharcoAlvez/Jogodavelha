import sys
import random

#Onde o X e O vao entrar
board = [["", "", ""], ["", "", ""], ["", "", ""]]

#Declara onde o jogo começa
exampleBoard = [[1,2,3], [4,5,6], [7,8,9]]


gameWon = 0

#Funçao que faz a velha
def displayBoard():
    global board
    print (board[0][0]," |",board[0][1],"  |", board[0][2])
    print ('------------')
    print (board[1][0]," |",board[1][1],"  |", board[1][2])
    print ('------------')
    print (board[2][0]," |",board[2][1],"  |", board[2][2])

#Essa funcao entra com o jogador 1 e onde ele quer marcar
def playerInput():
    global board
    global marker

    print("Jogador um, sua vez - X", "\n")

    marker = "X"
    row = int(input("Em qual linha deseja jogar?(1-3): "))
    col = int(input("Em qual coluna deseja jogar??(1-3): "))

    if board[row - 1][col - 1] == "":
        board[row - 1][col -1] = marker
    else:
        print("Essa posição está ocupada, tenta outra!")
        playerInput()

#TEssa funcao entra com o segundo jogador e onde ele quer marcar
def playerTwoInput():
    global board
    global marker

    print("Hey, it's the computer's turn - O", "\n")
    marker = "O"
    row = int(random.randint(1,3))
    col = int(random.randint(1,3))

    if board[row - 1][col - 1] == "":
        board[row - 1][col -1] = marker
    else:
        print("Essa posição está ocupada, tente outra!")
        playerTwoInput()

def Jogadordoisentrada():
    global board
    global marker

    print("Jogador dois, sua vez! - O", "\n")
    marker = "O"
    row = int(input("Qual linha quer jogar?(1-3): "))
    col = int(input("Qual coluna quer jogar?(1-3): "))

    if board[row - 1][col - 1] == "":
        board[row - 1][col -1] = marker
    else:
        print("Essa posição está ocupada, tente outra!")
        Jogadordoisentrada()

#Funcao que pergunta se quer jogar de novo ou nao
def rematch():
    global board
    global gameWon
    ans = input("Quer jogar outra vez? Y or N: ")

    print(ans)

    
    if ans == "Y" or ans == "y":
        board = [["", "", ""], ["", "", ""], ["", "", ""]]

        gameWon = 0
        runCode()

    elif ans == "N" or ans == "n":
        print("Obrigado por jogar!")
    else: 
        print("Obrigado por jogar!")

#funcao que checa quem ganhou o jogo
def checkGameStatus():
    global board
    global gameWon
    if board[0][0] == board[1][1] == board[2][2] == marker or board[0][2] == board[1][1] == board[2][0] == marker:
        gameWon = 1
        print("{playerI} É o vencedos!".format(playerI = marker))

        rematch()
        sys.exit()
    elif board[0][0] == board[0][1] == board[0][2] == marker or board[0][1] == board[1][1] == board[2][1] == marker:
        gameWon = 1
        print("{playerI} É o vencedor!".format(playerI = marker))
        rematch()
        sys.exit()
    elif board[1][0] == board[1][1] == board[1][2] == marker or board[2][0] == board[2][1] == board[2][2] == marker:
        gameWon = 1
        print("{playerI} É o vencedor!".format(playerI = marker))
        rematch()
        sys.exit()
    elif board[0][0] == board[1][0] == board[2][0] == marker or board[0][2] == board[1][2] == board[2][2] == marker:
        gameWon = 1
        print("{playerI} É o vencedor!".format(playerI = marker))
        rematch()
        sys.exit()

    return

#Funcao que roda o jogo
def runCode():
    x = 0

    while x < 4:
        playerInput()
        displayBoard()
        checkGameStatus()
        # playerTwoInput()
        Jogadordoisentrada()
        displayBoard()
        checkGameStatus()

        x += 1
    if gameWon == 0:
        playerInput()
        displayBoard()
        checkGameStatus()
    print("Deu velha. ")
    rematch()

print("É uma borda simples de três linhas e três colunas. ")

print (exampleBoard[0][0]," |",exampleBoard[0][1],"  |", exampleBoard[0][2])
print ('------------')
print (exampleBoard[1][0]," |",exampleBoard[1][1],"  |", exampleBoard[1][2])
print ('------------')
print (exampleBoard[2][0]," |",exampleBoard[2][1],"  |", exampleBoard[2][2])
runCode()
