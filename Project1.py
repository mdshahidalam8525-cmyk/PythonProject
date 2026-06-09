
#? This function for board
def dispaly_board(board):
    print('\n'*10)
    print(board[1]+' | '+board[2]+' | '+board[3]  )
    print('--+---+--')
    print(board[4]+' | '+board[5]+' | '+board[6]  )
    print('--+---+--')
    print(board[7]+' | '+board[8]+' | '+board[9]  )
    print('\n'*3)

#? This function for assing symbol
def player_input():
    marker = ' '
    while marker not in ['X','O']:
        marker = input("player_1 choose (X OR O): ").upper()
    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')
    

def game_start():
    while True:
        try:
            ready = input("Are You ready to Play?,(Yes Or Not): ").upper()
            if ready.startswith('Y'):
                return True
            elif ready.startswith('N'):
                return False
        except:
            print("Plz choose vailid input (Yes Or Not): ")
    

#? This function for place marker
def place_marker(board,mark,position):
    board[position] = mark


#? This function check all winning condition
def win_check(board,mark):
    return((board[1] == board[2] == board[3] == mark) or
           (board[4] == board[5] == board[6] == mark) or
           (board[7] == board[8] == board[9] == mark) or
           (board[1] == board[4] == board[7] == mark) or
           (board[2] == board[5] == board[8] == mark) or
           (board[3] == board[6] == board[9] == mark) or
           (board[1] == board[5] == board[9] == mark) or
           (board[3] == board[5] == board[7] == mark))


#? This function for random olayer choice
import random
def choose_first():
    return random.choice(["player_1","player_2"])


#? This functon check board have space or not
def space_check(board,position):
    return board[position] == " "


#? This function check board is full or not
def full_board_check(board):
    for pos in range(1,10):
        if space_check(board,pos):
            return False
    return True


#? This function for player position from (1 to 9)
def player_choice(board):
    while True:
        try:
            position = int(input("Plz choose Your position (1 To 9): "))
            if position not in range(1,10):
                print("Plz choose your position (1 To 9): ")

            elif not space_check(board,position):
                print("Position already accupied: ")
            
            else:
                return position
            
        except:
            print("choose a vailid possition between (1 to 9): ")


#? This function for replay
def replay():
    while True:
        play_mode = input("Play again (Yes OR Not): ").strip().upper()
        if play_mode.startswith('Y'):
            return True
        elif play_mode.startswith('N'):
            return False
        else:
            print("Do You want play again? \n" \
            "Choose a vailid input: ")



#? Main game loop
print("Welcome To Tic Tac Toe Game!")
while True:
    test_board = [' ']*10

    player_1,player_2 = player_input()

    turn = choose_first()
    print(f"{turn} will go first! ")

    game_on = game_start()
    while game_on == False:
        print("Thanks for Your response!")
        break

    while game_on:
        
        if turn == 'player_1':
            dispaly_board(test_board)
            position = player_choice(test_board)
            place_marker(test_board,player_1,position)

            if win_check(test_board,player_1):
                dispaly_board(test_board)
                print("Player_1 win!")
                game_on = False


            elif full_board_check(test_board):
                dispaly_board(test_board)
                print("game draw")
                game_on = False

            else:
                turn = "player_2"

        else:
            dispaly_board(test_board)
            position = player_choice(test_board)
            place_marker(test_board,player_2,position)

            if win_check(test_board,player_2):
                dispaly_board(test_board)
                print("Player 2 win!")
                game_on = False

            elif full_board_check(test_board):
                dispaly_board(test_board)
                print("Game Draw!")
                game_on = False

            else:
                turn = "player_1"

    if not replay():
        print("Thanks for playing!")
        break