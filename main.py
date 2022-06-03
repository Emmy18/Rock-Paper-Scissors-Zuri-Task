import random

possible_options = ["R", "P", "S"]

print("You're to choose any option between R, P or S. R for Rock, P for Paper and S for Scissors. To end the game, Type 'End'")

CPU_score = 0
player_score = 0

while True:
    player = input("What's your preferred choice: ").capitalize()
    CPU = random.choice(possible_options)
    if player not in possible_options:
        print("Wrong option! Choose any of R, P or S")
    if player == CPU:
        print("Player chose", player)
        print("The computer chose", CPU)
        print("Therefore, its a Tie!")
    elif player == "R":
        if CPU == "P":
            print("Player chose", player)
            print("The computer chose", CPU)
            print("Therefore,You Lost this round!")
            CPU_score += 1
        else:
            print("Player chose", player)
            print("The computer chose", CPU)
            print("Therefore,You won this round!")
            player_score += 1
    elif player == "P":
        if CPU == "S":
            print("Player chose", player)
            print("The computer chose", CPU)
            print("Therefore, You Lost this round!")
            CPU_score += 1
        else: 
            print("Player chose", player)
            print("The computer chose", CPU)
            print("Therefore, You won this round!")
            player_score += 1
    elif player == "S":
        if CPU == "R":
            print("Player chose", player)
            print("The computer chose", CPU)
            print("Therefore, You Lost this round!")
            CPU_score += 1
        else: 
            print("Player chose", player)
            print("The computer chose", CPU)
            print("Therefore, You won this round!")
            player_score += 1
    elif player == "End":
        print("There's are the Final Scores: \nCPU scored: ",CPU_score, "\nPlayer scored: ", player_score)
        if player_score == CPU_score:
            print("We have no winner, Game continue!")
            continue
        elif player_score > CPU_score:
            print("Player is the winner")
        else: print("CPU is the winner")
        break