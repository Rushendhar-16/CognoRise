import random

def roll_dice(num_sides, num_rolls):
    """
    Simulates rolling a die with num_sides sides, num_rolls times.

    Args:
    num_sides (int): Number of sides on the die.
    num_rolls (int): Number of times to roll the die.

    Returns:
    list: A list of results from the rolls.
    """
    results = []
    for _ in range(num_rolls):
        roll_result = random.randint(1, num_sides)
        results.append(roll_result)
    return results

def main():
    print("Welcome to the Dice Rolling Simulator!")
    
    # Get user input for number of sides on the dice
    num_sides = int(input("Enter the number of sides on the dice: "))
    
    # Get user input for number of rolls
    num_rolls = int(input("Enter the number of rolls: "))
    
    # Roll the dice and get the results
    results = roll_dice(num_sides, num_rolls)
    
    # Display the results
    print(f"Rolling a {num_sides}-sided dice {num_rolls} times...")
    for i, result in enumerate(results, start=1):
        print(f"Roll {i}: {result}")

if __name__ == "__main__":
    main()
