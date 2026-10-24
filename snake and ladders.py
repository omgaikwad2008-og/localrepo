import random


SNAKES = {
    99: 54,
    95: 72,
    92: 88,
    89: 68,
    74: 53,
    64: 42,
    62: 19,
    49: 11,
    46: 25,
    16: 6,
}

LADDERS = {
    2: 38,
    7: 14,
    8: 31,
    15: 26,
    21: 42,
    28: 84,
    36: 44,
    51: 67,
    71: 91,
    78: 98,
    87: 94,
}


def roll_dice():
    return random.randint(1, 6)


def show_rules():
    print("\n--- Snake and Ladders Rules ---")
    print("1. Reach square 100 to win.")
    print("2. Roll a 6 to get another turn.")
    print("3. If you land on a ladder, you climb up.")
    print("4. If you land on a snake, you slide down.")
    print("5. You need the exact number to reach 100.\n")


def print_board(players):
    """Print a simple board with player locations."""
    player_at = {}

    for player, position in players.items():
        if position not in player_at:
            player_at[position] = []
        player_at[position].append(player)

    print("\n" + "=" * 57)

    for row in range(9, -1, -1):
        numbers = list(range(row * 10 + 1, row * 10 + 11))

        # Reverse every alternate row for snake-board style.
        if row % 2 == 1:
            numbers.reverse()

        for number in numbers:
            labels = player_at.get(number, [])

            if labels:
                cell = "".join(labels)
                print(f"{number:>3}[{cell:<2}]", end=" ")
            else:
                print(f"{number:>3}    ", end=" ")

        print("\n")

    print("=" * 57)


def move_player(name, position, dice):
    """Move a player and apply snakes or ladders."""
    new_position = position + dice

    if new_position > 100:
        print(f"{name} needs an exact roll to reach 100.")
        return position

    print(f"{name} moves from {position} to {new_position}.")

    if new_position in LADDERS:
        new_position = LADDERS[new_position]
        print(f"🎉 Ladder! {name} climbs up to {new_position}.")

    elif new_position in SNAKES:
        new_position = SNAKES[new_position]
        print(f"🐍 Snake! {name} slides down to {new_position}.")

    return new_position


def get_number_of_players():
    while True:
        try:
            number = int(input("How many players? (2-4): "))

            if 2 <= number <= 4:
                return number

            print("Please choose between 2 and 4 players.")

        except ValueError:
            print("Enter a valid number.")


def get_player_names(number_of_players):
    players = {}

    for number in range(1, number_of_players + 1):
        while True:
            name = input(f"Enter name for Player {number}: ").strip()

            if not name:
                print("Name cannot be empty.")
            elif name in players:
                print("This name is already used.")
            else:
                players[name] = 0
                break

    return players


def main():
    print("=" * 35)
    print("      SNAKE AND LADDERS")
    print("=" * 35)

    show_rules()

    number_of_players = get_number_of_players()
    players = get_player_names(number_of_players)

    player_names = list(players.keys())
    current_player_index = 0

    print("\nGame begins!")
    print_board(players)

    while True:
        current_player = player_names[current_player_index]

        input(f"\n{current_player}'s turn. Press Enter to roll the dice...")

        dice = roll_dice()
        print(f"{current_player} rolled: {dice}")

        players[current_player] = move_player(
            current_player,
            players[current_player],
            dice,
        )

        print_board(players)

        if players[current_player] == 100:
            print(f"\n🏆 {current_player} wins the game! 🏆")
            break

        # A six gives the same player another turn.
        if dice == 6:
            print(f"{current_player} rolled a 6, so they play again!")
        else:
            current_player_index = (
                current_player_index + 1
            ) % len(player_names)


if __name__ == "__main__":
    main()