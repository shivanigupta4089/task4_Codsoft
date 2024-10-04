import random
while True:
    users_choice = input("\nEnter a choice (rock, paper, scissor): ")
    possibilities = ["rock", "paper", "scissor"]
    computer_choice = random.choice(possibilities)
    print(f"You are chosen {users_choice}, computer has choosen {computer_choice}")

    if users_choice == computer_choice:
        print(f"Both players selected {users_choice}. It's a tie")
    elif users_choice == "rock":
        if computer_choice == "scissor":
            print("Rock smashes scissor! You win")
        else:
            print("Paper covers rock! You lose")
    elif users_choice == "paper":
        if computer_choice == "rock":
            print("Paper covers rock! You win")
        else:
            print("Scissor cuts paper! You lose")
    elif users_choice == "scissor":
        if computer_choice == "paper":
            print("Scissors cuts paper! You win")
        else:
            print("Rock smashes scissor! You lose")
    play_again = input("\nPlay again? (yes/no): ")
    if play_again.lower() != "yes":
        break
