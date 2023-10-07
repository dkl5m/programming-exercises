player_victories = 0
machine_victories = 0

def PLayer_Option():
    player_choice = input("Choose between rock, paper and scissors:")

while True:

    player_choice = input("Do you want to play again?'")
    if player_choice in ["Yes", "yes", "y", "Y"]:
        pass
    elif player_choice in {"No", "no", "n", "N"}:
        break
    else:
        break