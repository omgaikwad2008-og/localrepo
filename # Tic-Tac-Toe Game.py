# Tic-Tac-Toe Game

board = [" " for _ in range(9)]


def print_board():
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()


def check_winner(player):
    winning_positions = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6],
    ]

    for positions in winning_positions:
        if all(board[position] == player for position in positions):
            return True

    return False


def is_draw():
    return " " not in board


def get_move(player):
    while True:
        try:
            move = int(input(f"Player {player}, choose a position (1-9): ")) - 1

            if move < 0 or move > 8:
                print("Choose a number from 1 to 9.")
            elif board[move] != " ":
                print("That position is already taken.")
            else:
                return move

        except ValueError:
            print("Please enter a number.")


def main():
    current_player = "X"

    print("Welcome to Tic-Tac-Toe!")
    print("Positions are numbered from 1 to 9:")
    print("""
 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9
""")

    while True:
        print_board()

        move = get_move(current_player)
        board[move] = current_player

        if check_winner(current_player):
            print_board()
            print(f"Player {current_player} wins!")
            break

        if is_draw():
            print_board()
            print("It's a draw!")
            break

        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"


if __name__ == "__main__":
    main()