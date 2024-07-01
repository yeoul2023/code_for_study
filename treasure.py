print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇\

# def ts_game():
#     while True:
#         first_case = input("left or right?: ").lower()
#         if first_case == "right":
#             print("Game Over")
#             continue

#         second_case = input("swim or wait?: ").lower()
#         if second_case == "swim":
#             print("Game Over")
#             continue

#         third_case = input("Which door? Red, Blue or Yellow: ").lower()
#         if third_case == "red":
#             print("Game Over")
#             continue
#         elif third_case == "blue":
#             print("Game Over")
#             continue
#         elif third_case == "yellow":
#             print("You Win!")
#             break
#         else:
#             print("문도 제대로 못 고르냐")
#             continue

import time


def ts_game():
    while True:
        first_case = input("left or right?: ").strip().lower()
        if first_case == "left":
            second_case = input("swim or wait?: ").strip().lower()
            if second_case == "wait":
                third_case = input(
                    "Which door? Red, Blue or Yellow: ").strip().lower()
                if third_case == "red":
                    print("Burned by fire. Game over.")
                elif third_case == "Blue":
                    print("Eaten by beasts. Game over.")
                elif third_case == "yellow":
                    print("you win!!")
                    break
                else:
                    print("Invalid choice. Game over")
                    continue
            elif second_case == "swim":
                print("Game Over")
                continue
            else:
                print("어휴...넌 그냥 꺼져라")
                break

        elif first_case == "right":
            print("Game Over")
            break

        else:
            print("어휴...넌 그냥 꺼져라")
            break


def get_play_time():
    start_time = time.time()
    ts_game()
    end_time = time.time()
    play_time = end_time - start_time
    return play_time


def main():
    player_name = input("What's your name? : ")
    print(f"Welcome, {player_name}!")

    while True:
        start_answer = input(f"{player_name}, would you like to start? (Y/N): "
                             ).strip().lower()

        if start_answer == "y":
            play_time = get_play_time()
            print(f"게임 플레이 시간: {play_time:.2f} 초")
            break
        elif start_answer == "n":
            print("알겠습니다. 다음에 다시 만나요.")
            break
        else:
            print("잘못된 입력입니다. Y 또는 N을 입력해주세요.")


if __name__ == "__main__":
    main()
