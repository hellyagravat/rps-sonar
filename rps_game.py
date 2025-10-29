import random

# Track player choices
count_rock = 0
count_paper = 0
count_scissors = 0

# Track scores
player_score = 0
computer_score = 0


# === FUNCTION: Update player move counts ===
def update_count(user_input):
    global count_rock, count_paper, count_scissors
    if user_input == "rock":
        count_rock += 1
    elif user_input == "paper":
        count_paper += 1
    elif user_input == "scissors":
        count_scissors += 1


# === FUNCTION: Predict player's next move and counter it ===
def predict():
    global count_rock, count_paper, count_scissors

    # If player uses one move most frequently, computer counters it
    if count_rock > count_paper and count_rock > count_scissors:
        return "paper"  # paper beats rock
    elif count_paper > count_rock and count_paper > count_scissors:
        return "scissors"  # scissors beats paper
    elif count_scissors > count_rock and count_scissors > count_paper:
        return "rock"  # rock beats scissors
    else:
        # If tied or no data, choose randomly
        return random.choice(["rock", "paper", "scissors"])


# === FUNCTION: Determine round result ===
def play_round(player_choice, computer_choice):
    global player_score, computer_score

    print(f"\nYou played {player_choice}.")
    print(f"Computer played {computer_choice}.")

    # Determine winner
    if player_choice == computer_choice:
        print("It's a tie!")
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        print("You win this round!")
        player_score += 1
    else:
        print("Computer wins this round!")
        computer_score += 1

    # Display scores
    print(f"Your Score: {player_score} | Computer Score: {computer_score}")
    print("-" * 40)


# === MAIN GAME LOOP ===
def play_game():
    global player_score, computer_score

    print(" Welcome to Rock, Paper, Scissors!")
    print("First to reach 10 points wins.")
    print("Enter: R for Rock | P for Paper | S for Scissors")

    valid_entries = {"r": "rock", "p": "paper", "s": "scissors"}

    while player_score < 10 and computer_score < 10:
        # Get valid user input
        user_input = input("\nEnter your choice: ").lower().strip()
        if user_input not in valid_entries and user_input not in ["rock", "paper", "scissors"]:
            print(" Invalid input. Please enter R, P, or S (or full word).")
            continue

        # Normalize input
        if user_input in valid_entries:
            user_input = valid_entries[user_input]

        # Update the count for prediction
        update_count(user_input)

        # Computer predicts and counters player move
        computer_choice = predict()

        # Play one round
        play_round(user_input, computer_choice)

    # === END GAME RESULT ===
    if player_score == 10:
        print("\n Congratulations! You won the game!")
    else:
        print("\n Computer won the game! Better luck next time!")


# Run the game
if __name__ == "__main__":
    play_game()
