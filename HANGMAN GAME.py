import random

# Word list for the game
word_list = ["python", "java", "kotlin", "javascript", "hangman", "programming"]

# Hangman display stages
hangman_stages = [
    """
     -----
     |   |
         |
         |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """
]

def select_random_word(word_list):
    return random.choice(word_list)

def display_game_state(word_state, incorrect_guesses, hangman_stage):
    print(hangman_stage)
    print("Word: " + " ".join(word_state))
    print("Incorrect guesses: " + ", ".join(incorrect_guesses))

def play_hangman():
    word_to_guess = select_random_word(word_list)
    word_state = ["_" for _ in word_to_guess]
    incorrect_guesses = []
    correct_guesses = set()
    max_incorrect_guesses = len(hangman_stages) - 1
    current_stage = 0

    while current_stage < max_incorrect_guesses:
        display_game_state(word_state, incorrect_guesses, hangman_stages[current_stage])
        
        guess = input("Guess a letter: ").lower()
        
        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single letter.")
            continue
        
        if guess in correct_guesses or guess in incorrect_guesses:
            print("You've already guessed that letter.")
            continue
        
        if guess in word_to_guess:
            correct_guesses.add(guess)
            for idx, letter in enumerate(word_to_guess):
                if letter == guess:
                    word_state[idx] = guess
        else:
            incorrect_guesses.append(guess)
            current_stage += 1

        if "_" not in word_state:
            display_game_state(word_state, incorrect_guesses, hangman_stages[current_stage])
            print("Congratulations! You've guessed the word!")
            break
    else:
        display_game_state(word_state, incorrect_guesses, hangman_stages[current_stage])
        print(f"Game Over! The word was: {word_to_guess}")

def main():
    while True:
        play_hangman()
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break
    print("Thanks for playing Hangman!")

if __name__ == "__main__":
    main()
