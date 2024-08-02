import random

def real_name():
    return "harshit"

def name():
    user_name = input("Enter your name: ").lower()
    if user_name == real_name():
        return "\033[1;32mWelcome Boss\033[0m"  # Green text for the boss
    else:
        return f"Hello {user_name}"

def get_user_choice():
    user_choice = input("Enter a choice (\033[1;34mrock\033[0m, \033[1;34mpaper\033[0m, or \033[1;34mscissors\033[0m): ").lower()
    while user_choice not in ['rock', 'paper', 'scissors']:
        user_choice = input("Invalid choice. Please enter rock, paper, or scissors: ").lower()
    return user_choice

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "\033[1;33mIt's a tie!\033[0m"  # Yellow text for a tie
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "\033[1;32mYou win!\033[0m"  # Green text for a win
    else:
        return "\033[1;31mComputer wins!\033[0m"  # Red text for a loss

def play_game():
    print(name())
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"\nYou chose \033[1;34m{user_choice}\033[0m, computer chose \033[1;34m{computer_choice}\033[0m.")
    print(determine_winner(user_choice, computer_choice))
    print("\033[1;36m******PLAY AGAIN******\033[0m")  # Cyan text for play again
   

if __name__ == "__main__":
    play_game()
