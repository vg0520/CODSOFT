import random

# Initialize scores
user_score = 0
computer_score = 0

# Make functionto to get computer choice
def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

# Make function to find winner
def decide_winner(user, computer):
    if user == computer:
        return 'tie'
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'scissors' and computer == 'paper') or \
         (user == 'paper' and computer == 'rock'):
        return 'user'
    else:
        return 'computer'

# Make function to play game and run other function accordingly
def play_game():
    global user_score, computer_score

    print("Welcome to Rock-Paper-Scissors!")
    user = input("Choose rock, paper, or scissors: ").lower()
    if user not in ['rock', 'paper', 'scissors']:
        print("Invalid choice! Please choose rock, paper, or scissors.")
        return play_game()

    computer = get_computer_choice()
    print(f"Computer chose: {computer}")
    result = decide_winner(user, computer)

    if result == 'tie':
        print("It's a tie!")
    elif result == 'user':
        print("You win this round!")
        user_score += 1
    else:
        print("Computer wins this round.")
        computer_score += 1

    print(f"\nCurrent Score — You: {user_score} | Computer: {computer_score}")
    
    again = input("Do you want to play again? (yes/no): ").lower()
    if again == 'yes':
        play_game()
    else:
        print("\n Final Score:")
        print(f" You: {user_score} | Computer: {computer_score}")
        print("Thanks for playing!")

# Start the game
play_game()