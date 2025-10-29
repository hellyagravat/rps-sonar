import random

# Function to determine the winner
def get_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'scissors' and computer_choice == 'paper') or \
         (player_choice == 'paper' and computer_choice == 'rock'):
        return "Player wins!"
    else:
        return "Computer wins!"

# Function to get the computer's choice
def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

# Main game loop
def play_game():
    player_score = 0
    computer_score = 0

    print("Welcome to Rock, Paper, Scissors!")

    while player_score < 10 and computer_score < 10:
        # Get user input
        user_input = input("Enter your choice (rock, paper, or scissors): ").lower()
        
        # Input validation
        if user_input not in ['rock', 'paper', 'scissors']:
            print("Invalid input. Please enter 'rock', 'paper', or 'scissors'.")
            continue

        # Get computer's choice
        computer_choice = get_computer_choice()

        # Print choices
        print(f"You played {user_input}.")
        print(f"Computer played {computer_choice}.")

        # Determine the winner
        result = get_winner(user_input, computer_choice)
        print(result)

        # Update scores based on the result
        if result == "Player wins!":
            player_score += 1
        elif result == "Computer wins!":
            computer_score += 1

        # Print scores
        print(f"Player Score: {player_score}")
        print(f"Computer Score: {computer_score}")
        print("------------------------------")

    # End game
    if player_score == 10:
        print("Congratulations! You won the game!")
    else:
        print("Sorry, the computer won the game!")

# Start the game
play_game()
