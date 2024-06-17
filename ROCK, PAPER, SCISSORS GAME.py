import random

def get_user_choice():
    choices = ["rock", "paper", "scissors"]
    while True:
        user_choice = input("Enter rock, paper, or scissors: ").lower()
        if user_choice in choices:
            return user_choice
        else:
            print("Invalid choice. Please try again.")

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "win"
    else:
        return "lose"

def display_result(user_choice, computer_choice, result):
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    if result == "win":
        print("You win!")
    elif result == "lose":
        print("You lose.")
    else:
        print("It's a tie.")

def play_game():
    user_score = 0
    computer_score = 0
    
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)
        display_result(user_choice, computer_choice, result)
        
        if result == "win":
            user_score += 1
        elif result == "lose":
            computer_score += 1

        print(f"\nScores -> You: {user_score} | Computer: {computer_score}")

        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

    print("\nThank you for playing! Final Scores -> You: {} | Computer: {}".format(user_score, computer_score))

if __name__ == "__main__":
    play_game()
