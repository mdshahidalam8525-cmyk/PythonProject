import random


def display_board(board):
    print("\n")
    print(board[7] + " | " + board[8] + " | " + board[9])
    print("--+---+--")
    print(board[4] + " | " + board[5] + " | " + board[6])
    print("--+---+--")
    print(board[1] + " | " + board[2] + " | " + board[3])
    print("\n")


def player_input():
    marker = ""

    while marker not in ("X", "O"):
        marker = input("Player 1, choose X or O: ").upper()

    if marker == "X":
        return "X", "O"
    else:
        return "O", "X"


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    return (
        (board[7] == board[8] == board[9] == mark) or
        (board[4] == board[5] == board[6] == mark) or
        (board[1] == board[2] == board[3] == mark) or
        (board[7] == board[4] == board[1] == mark) or
        (board[8] == board[5] == board[2] == mark) or
        (board[9] == board[6] == board[3] == mark) or
        (board[7] == board[5] == board[3] == mark) or
        (board[9] == board[5] == board[1] == mark)
    )


def choose_first():
    return random.choice(["Player 1", "Player 2"])


def space_check(board, position):
    return board[position] == " "


def full_board_check(board):
    for pos in range(1, 10):
        if space_check(board, pos):
            return False
    return True


def player_choice(board):
    while True:
        try:
            position = int(input("Choose a position (1-9): "))

            if position not in range(1, 10):
                print("Please enter a number between 1 and 9.")

            elif not space_check(board, position):
                print("That position is already occupied.")

            else:
                return position

        except ValueError:
            print("Please enter a valid number.")


def replay():
    return input("Play again? (Yes/No): ").lower().startswith("y")


# Main Game Loop
print("Welcome to Tic Tac Toe!")

while True:

    board = [" "] * 10

    player1_marker, player2_marker = player_input()

    turn = choose_first()
    print(f"\n{turn} will go first!")

    ready = input("Are you ready to play? (Yes/No): ").lower()

    game_on = ready.startswith("y")

    while game_on:

        if turn == "Player 1":

            display_board(board)

            position = player_choice(board)

            place_marker(board, player1_marker, position)

            if win_check(board, player1_marker):
                display_board(board)
                print("🎉 Player 1 Wins!")
                game_on = False

            elif full_board_check(board):
                display_board(board)
                print("🤝 It's a Draw!")
                game_on = False

            else:
                turn = "Player 2"

        else:

            display_board(board)

            position = player_choice(board)

            place_marker(board, player2_marker, position)

            if win_check(board, player2_marker):
                display_board(board)
                print("🎉 Player 2 Wins!")
                game_on = False

            elif full_board_check(board):
                display_board(board)
                print("🤝 It's a Draw!")
                game_on = False

            else:
                turn = " Player 1"

    if not replay():
        print("Thanks for playing!")
        break