import random

print("Welcome to Rock-Paper-Scissors game! \n1. To play in a SINGLE PLAYER mode - press 's'"
      "\n2. To play in a MULTIPLAYER mode (2 players) - press 'm'")
list_of_opp = ["rock", "paper", "scissors"]
option = input()

player1_result = 0
player2_result = 0

again = True
numb_of_rounds = 3
# Single Player
while again:
    if option == "s":
        player = input("Let's start! Choose one of them: 'rock', 'paper' or 'scissors' ")
        computer_play = str(random.choice(list_of_opp))
        if player == "rock" and computer_play == "paper":
            print("Computer picked: " + computer_play + ". You lose!")
        elif player == "paper" and computer_play == "scissors":
            print("Computer picked: " + computer_play + ". You lose!")
        elif player == "scissors" and computer_play == "rock":
            print("Computer picked: " + computer_play + ". You lose!")
        elif player == computer_play:
            print("Computer picked: " + computer_play + ". It's a draw!")
        elif player not in list_of_opp:
            print("Invalid typing.")
        else:
            print("Computer picked: " + computer_play + ". You win! Congratulations!")

#Multiplayer
    if option == "m":
        while numb_of_rounds != 0:
            player1 = input("Player 1 choosing: 'rock', 'paper' or 'scissors' ")
            player2 = input("Player 2 choosing: 'rock', 'paper' or 'scissors' ")

            printing_results = ("\nPlayer 1: " + player1 + " Player 2: " + player2)

            if player1 == "rock" and player2 == "paper":
                player2_result += 1
                print(printing_results)
                numb_of_rounds -= 1
            elif player1 == "paper" and player2 == "scissors":
                player2_result += 1
                print(printing_results)
                numb_of_rounds -= 1
            elif player1 == "scissors" and player2 == "rock":
                player2_result += 1
                print(printing_results)
                numb_of_rounds -= 1
            elif player1 == player2:
                player1_result += 1
                player2_result += 1
                print(printing_results)
                numb_of_rounds -= 1
            elif (player1 and player2) not in list_of_opp:
                print("Invalid typing.")
            else:
                player1_result += 1
                print(printing_results)
                numb_of_rounds -= 1
            print("Score: " + str(player1_result) + " : " + str(player2_result))
    repeat = input("\nAgain? y/n ")
    if repeat == "y":
        again = True
    else:
        print("Thanks for playing! See ya!")
        again = False
        break
