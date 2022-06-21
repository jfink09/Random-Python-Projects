import random

while True:
    choices = ['rock', 'paper', 'scissors']

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("Rock, Paper, or Scissors? ").lower()

    if player == computer:
     print("Player: " + player)
     print("Computer: " + computer)
     print("You tie.")
    elif player == "rock":
        if computer == "paper":
            print("Player: " + player)
            print("Computer: " + computer)
            print("You lose.")
        if computer == "scissors":
            print("Player: " + player)
            print("Computer: " + computer)
            print("You win.")
    elif player == "scissors":
        if computer == "paper":
            print("Player: " + player)
            print("Computer: " + computer)
            print("You win.")
        if computer == "rock":
            print("Player: " + player)
            print("Computer: " + computer)
            print("You lose.")
    elif player == "paper":
        if computer == "scissors":
            print("Player: " + player)
            print("Computer: " + computer)
            print("You lose.")
        if computer == "rock":
            print("Player: " + player)
            print("Computer: " + computer)
            print("You win.")

    play_again = input("Play again? (yes/no): ").lower()

    if play_again != "yes":
        break

print("Ok.")
