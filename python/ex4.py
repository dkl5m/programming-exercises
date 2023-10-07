# ROCK, PAPER, SCISSORS GAME - PYTHON EDITION
from random import choice

player_victories = 0
machine_victories = 0


def Player_Option():
    player_choice = input("Choose between rock, paper and scissors: ")
    player_choice.lower()
    if player_choice == "rock":
        return player_choice
    elif player_choice == "paper":
        return player_choice
    elif player_choice == "scissors":
        return player_choice
    else:
        print("Invalid choice. Try again! ")
        Player_Option()


def Machine_Option():
    machine_choice = choice(["rock", "paper", "scissors"])
    return machine_choice


while True:
    print("-"*30)
    player_choice = Player_Option()
    machine_choice = Machine_Option()
    print("-"*30)

    # player wins
    if (player_choice == "rock") and (machine_choice == "scissors") \
        or (player_choice == "scissors") and (machine_choice == "paper") \
            or (player_choice == "paper") and (machine_choice == "rock"):
        print(f"Your choice: {player_choice}. Machine choice: "
              f"{machine_choice}. You won!")
        player_victories += 1
    # draw
    elif (player_choice == machine_choice):
        print(f"Your choice: {player_choice}. Machine choice: "
              f"{machine_choice}. Draw!")
    # machine wins
    else:
        print(f"Your choice: {player_choice}. Machine choice: "
              f"{machine_choice}. Machine Won!")
        machine_victories += 1

    print("-"*30)
    print(f"Player Victories: {player_victories}.")
    print(f"Machine Victories: {machine_victories}.")
    print("-"*30)

    player_choice = input("Do you want to play again?'")
    if player_choice in ["YES", "Yes", "yes", "y", "Y"]:
        pass
    elif player_choice in {"NO", "No", "no", "n", "N"}:
        break
    else:
        break
