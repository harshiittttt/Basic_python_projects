import random


def main():
    print("Welcome to Rock, Paper, and Scissors!")
    print("First to score 5 points wins the game!")
    user_score = 0
    comp_score = 0

    # Mapping numbers to choices
    choices = {1: "Rock", 2: "Paper", 3: "Scissors"}

    while True:
        print("\nYour Choices:")
        print("1. Rock\n2. Paper\n3. Scissors")

        # User Input
        try:
            user_choice = int(input("Please choose your option (1, 2, or 3): "))
            if user_choice not in [1, 2, 3]:
                print("Invalid input! Please choose 1, 2, or 3.")
                continue
        except ValueError:
            print("Invalid input! Please enter a number (1, 2, or 3).")
            continue

        # Computer's choice
        computer_input = random.randint(1, 3)
        print(f"\nYou chose: {choices[user_choice]}")
        print(f"Computer chose: {choices[computer_input]}")

        # Determining the winner
        if user_choice == computer_input:
            print("It's a Draw!")
        elif (user_choice == 1 and computer_input == 3) or \
                (user_choice == 2 and computer_input == 1) or \
                (user_choice == 3 and computer_input == 2):
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            comp_score += 1

        # Displaying the current score
        print(f"Scores - You: {user_score}, Computer: {comp_score}")

        # Checking if the game is over
        if user_score == 5:
            print("\nCongratulations! You won the game!")
            break
        elif comp_score == 5:
            print("\nGame Over! The computer won the game.")
            break

    print("\nFinal Scores:")
    print(f"You: {user_score}, Computer: {comp_score}")
    print("Thanks for playing! Goodbye!")


# Starting the game
main()
