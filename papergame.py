import random

# Function to get the player's choice and validate it
def get_user_choice():
    choice = input("Enter your choice (rock, paper, scissors): ").strip().lower()
    # Keep asking until the player enters a valid choice
    while choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please try again.")
        choice = input("Enter your choice (rock, paper, scissors): ").strip().lower()
    return choice

# Function to randomly select a choice for the computer
def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

# Function to determine the winner based on the choices
def determine_winner(choice1, choice2):
    if choice1 == choice2:
        return "Tie"
    elif (choice1 == "rock" and choice2 == "scissors") or \
         (choice1 == "scissors" and choice2 == "paper") or \
         (choice1 == "paper" and choice2 == "rock"):
             return "player 1 wins!"
    else:
        return "player 2 wins!"
    
# Main function to play the game
def game():
    # Loop to allow replaying the game until the player wants to stop
    while True:
        # Ask the player to choose the mode (against another player or the computer)
        mode = input("Do you want to play against another player or the computer? (player/computer): ").strip().lower()
        
        # Validate the mode choice
        while mode not in ["player", "computer", "p", "c"]:
            print("Invalid choice. Please try again.")
            mode = input("Do you want to play against another player or the computer? (player/computer): ").strip().lower()

        # Get Player 1's choice
        player1_choice = get_user_choice()

        # Choose the mode the player wants to play
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

# Run function     
if __name__ == "__main__":
    game()
            