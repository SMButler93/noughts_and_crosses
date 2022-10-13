import random

board = ['-', '-', '-', '-', '-', '-', '-', '-', '-']

player1_char = ""
player_2char = ""


def enter_name():
    """Gets users names"""
    username = input("Enter your username > ")
    print(f"Welcome to the game, {username}")
    return username


def assign_players():
    global player1_char
    global player2_char
    number = random.randint(0, 1)
    if number == 0:
        player1_char = "O"
        player2_char = "X"
    else:
        player1_char = "X"
        player2_char = "O"


def print_board():
    print(board[:3])
    print(board[3:6])
    print(board[6:])


def make_move(current_player, current_char):
    print(f"It's your move with, {current_char}, {current_player}")
    legal_move = False
    while legal_move == False:
        player_move = int(input("Enter your move, 1 to 9 >"))
        player_space = player_move - 1
        if board[player_space] == "-":
            board[player_space] = current_char
            legal_move = True
        else:
            print("That space is not empty. Please try again")


def check_win(current_char):
    if board[0] == current_char and board[1] == current_char and board[2] == current_char:
        return True
    elif board[3] == current_char and board[4] == current_char and board[5] == current_char:
        return True
    elif board[6] == current_char and board[7] == current_char and board[8] == current_char:
        return True
    elif board[0] == current_char and board[3] == current_char and board[6] == current_char:
        return True
    elif board[1] == current_char and board[4] == current_char and board[7] == current_char:
        return True
    elif board[2] == current_char and board[5] == current_char and board[8] == current_char:
        return True
    elif board[0] == current_char and board[4] == current_char and board[8] == current_char:
        return True
    elif board[2] == current_char and board[4] == current_char and board[6] == current_char:
        return True
    else:
        return False


# main program starts here
move_number = 1
game_over = False

player1_name = enter_name()
player2_name = enter_name()
assign_players()
print(player1_name, "you are playing", player1_char)
print(player2_name, "you are playing", player2_char)
print_board()

if player1_char == "O":
    current_player = player1_name
    current_char = player1_char
else:
    current_player = player2_name
    current_char = player2_char

while game_over is False and move_number <= 9:
    make_move(current_player, current_char)
    if check_win(current_char) == True:
        print_board()
        print(f"Congratulations {current_player} You have won!")
        game_over = True
    if current_player == player1_name:
        current_player = player2_name
        current_char = player2_char
    else:
        current_player = player1_name
        current_char = player1_char

    print_board()
    move_number = move_number+1

if game_over == False:
    print("It's a draw! Well done to you both!")
