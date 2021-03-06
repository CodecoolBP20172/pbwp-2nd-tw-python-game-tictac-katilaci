#upgrade:
# except: KeyboardInterrupt
# színek
# (grafikus felület)?
# ((egérhasználat))
# AI / akár több mód
# táblaméretet user adja meg
# score


def init_board():
    board = []
    for row in range(3):
        board.append([])
        for column in range(3):
            board[row].append(str(7 - row * 3 + column))
            #oszloponként, fentről lefele írja ki
    return board


def print_board(board):
    print("\n")
    for row in board:
        print(" ".join(row))



def take_step(actualplayer, player, board):
    valid = False
    while not valid:
        try:
            step = int(input("Player " + str(actualplayer + 1) + " (" + player[actualplayer] + ") take a step: "))
        except ValueError:
            print("Pick a number between 1 and 9!")
            continue
        if step in range(1,10):
            column = (step - 1) % 3
            row = int((7 - (step - column)) / 3)
            if board[row][column] == player[0] or board[row][column] == player[1]:
                print("Location already taken!")
            else:
                board[row][column] = player[actualplayer]
                valid = True
        else:
            print("Pick a number between 1 and 9!")

def switch_player(actualplayer):
    if actualplayer == 0:
        return 1
    else:
        return 0

def check_won(board, player, actualplayer):
    won = False
    sign = player[actualplayer]
    for i in range(3):
        column_won = board[0][i] == sign and board[1][i] == sign and board[2][i] == sign
        row_won = board[i][0] == sign and board[i][1] == sign and board[i][2] == sign
        won = won or column_won or row_won #  the won int so it keeps the new check value
    diagonal1_won = board[0][0] == sign and board[1][1] == sign and board[2][2] == sign
    diagonal2_won = board[2][0] == sign and board[1][1] == sign and board[0][2] == sign
    won = won or diagonal1_won or diagonal2_won
    if won:
        print("Player " +str(actualplayer + 1) +  " (" + player[actualplayer] + ") won!")
    return won



board = init_board()
player = ["X", "O"]
actualplayer = 0
step = 0
won = False

print_board(board)
while step < 9 and not won:
    take_step(actualplayer, player, board)
    print_board(board)
    won = check_won(board, player, actualplayer)
    actualplayer = switch_player(actualplayer)
    step = step + 1
if not won:
    print("Even!")
    except KeyboardInterrupt
        print("End")
# except (KeyboardInterrupt)
#     print("End")
