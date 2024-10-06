import random

def get_user_choice():
    choice = input("Enter your choice (rock, paper, scissors): ").strip().lower()
    while choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please try again.")
        choice = input("Enter your choice (rock, paper, scissors): ").strip().lower()
    return choice

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(choice1, choice2):
    if choice1 == choice2:
        return "Tie"
    elif (choice1 == "rock" and choice2 == "scissors") or \
         (choice1 == "scissors" and choice2 == "paper") or \
         (choice1 == "paper" and choice2 == "rock"):
             return "player 1 wins!"
    else:
        return "player 2 wins!"
    
def game():
    while True:
        mode = input("Do you want to play against another player or the computer? (player/computer): ").strip().lower()
        while mode not in ["player", "computer", "p", "c"]:
            print("Invalid choice. Please try again.")
            mode = input("Do you want to play against another player or the computer? (player/computer): ").strip().lower()

        player1_choice = get_user_choice()

        if mode == "computer":
            player2_choice = get_computer_choice()
            print(f"Computer chose: {player2_choice}")
        else:
            print("Player 2's turn.")
            player2_choice = get_user_choice()
            
        result = determine_winner(player1_choice, player2_choice)
        print(result)
        
        play_again = input("Play again? (yes/no): ").strip().lower()
        if play_again == "no" or play_again == "n":
            print("Thanks for playing!")
            break
        else:
            continue
        
if __name__ == "__main__":
    game()
            