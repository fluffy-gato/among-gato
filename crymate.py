import random
import sys

class Player:
    def __init__(self, name):
        self.name = name
        self.is_impostah = False
        self.tasks = []
        self.current_location = None

locations = ["Admin", "Cafeteria", "Storage", "MedBay", "Electrical"]

def print_players(players):
    print("Players:")
    for i, player in enumerate(players, start=1):
        print(f"{i}. {player.name} - Location: {player.current_location} - Tasks: {', '.join(player.tasks)}")

def print_location_menu():
    print("\nLocations:")
    for i, location in enumerate(locations, start=1):
        print(f"{i}. {location}")

def main():
    print("Welcome to Among Gato!")

    num_players = int(input("Enter the number of players: "))

    if num_players < 4:
        print("Among Gato requires at least 4 players. Exiting.")
        sys.exit(1)

    players = [Player(input(f"Enter name for player {i + 1}: ")) for i in range(num_players)]

    impostah_index = random.randint(0, num_players - 1)
    players[impostah_index].is_impostah = True

    print("\nThe game has started!")

    for player in players:
        player.current_location = random.choice(locations)
        player.tasks = random.sample(locations, k=2)

    while True:
        print_players(players)
        print_location_menu()

        try:
            player_index = int(input("Select a player to move (enter the corresponding number): ")) - 1
            location_index = int(input("Select a location to move to (enter the corresponding number): ")) - 1
        except (ValueError, IndexError):
            print("Invalid input. Please enter valid numbers.")
            continue

        if player_index < 0 or player_index >= num_players or location_index < 0 or location_index >= len(locations):
            print("Invalid selection. Please choose valid numbers.")
            continue

        player = players[player_index]
        player.current_location = locations[location_index]

        if player.current_location in player.tasks:
            player.tasks.remove(player.current_location)
            print(f"{player.name} completed a task at {player.current_location}!")

        if player.is_impostah:
            print("Impostah sabotages a task!")
            sabotaged_player = random.choice(players)
            sabotaged_player.tasks.append(random.choice(locations))
            print(f"{sabotaged_player.name}'s task in {sabotaged_player.tasks[-1]} is sabotaged!")

        if all(len(player.tasks) == 0 for player in players):
            print("All tasks completed. Crymates win!")
            break

if __name__ == "__main__":
    main()
