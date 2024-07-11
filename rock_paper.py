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

def rock_paper_sissor():
    choice = rd.choice(list(choices.keys())) # "rock", "paper", "scissors" 중 하나를 무작위로 선택
    return choice

def main():
    user_name = input("What's your name:")
    print(f"{user_name} Welcome!!")

    computer_choice = rock_paper_sissor()
    
    user_choice = input("choose rock, paper or scissors")
    while user_choice not in choices:
        print("잘못된 입력입니다.")
        user_choice = input("choose rock, paper or scissors")

    print(f"computer\n{choices[computer_choice]}")
    print(f"user\n{choices[user_choice]}")
    
    if user_choice == computer_choice:
         print("비겼습니다!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
         print(f"{user_name}님이 이겼습니다!")
    else:
         print("컴퓨터가 이겼습니다!")


main()