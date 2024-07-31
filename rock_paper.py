import random as rd

choices = {
    "rock": '''
        _______
    ---'   ____)
        (_____)
        (_____)
        (____)
    ---.__(___)
    ''',

    "paper": '''
        _______
    ---'   ____)__
            ______)
            _______)
            _______)
    ---.__________)
    ''',

    "scissors": '''
        _______
    ---'   ____)__
            ______)
        __________)
        (____)
    ---.__(___)
    '''
}

def get_computer_choice():
    return rd.choice(list(choices.keys()))

def get_user_choice():
    user_choice = input("Choose rock, paper, or scissors: ").strip().lower()
    while user_choice not in choices:
        print("Invalid input. Please choose again.")
        user_choice = input("Choose rock, paper, or scissors: ").strip().lower()
    return user_choice

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "User wins!"
    else:
        return "Computer wins!"
    
def main():
    computer_choice = get_computer_choice()
    user_choice = get_user_choice()

    print(f"Computer chose:\n{choices[computer_choice]}\n")
    print(f"You chose:\n{choices[user_choice]}\n")
    
    result = determine_winner(user_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    main()
