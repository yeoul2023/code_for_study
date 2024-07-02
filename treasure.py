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

import time


#게임 함수
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
                    return None
                elif third_case == "blue":
                    print("Eaten by beasts. Game over.")
                    return None
                elif third_case == "yellow":
                    print("you win!!")
                    return time.time() - start_time    #플레이 시간 반환
                else:
                    print("Invalid choice. Game over")
                    return None
            elif second_case == "swim":
                print("Game Over")
                return None
            else:
                print("Invalid choice. Game over.")
                return None

        elif first_case == "right":
            print("Game Over")
            return None

        else:
            print("Invalid choice. Game over.")
            return None


#게임 플레이 시간 측정 함수
def get_play_time():
    global start_time
    start_time = time.time()
    play_time = ts_game()
    end_time = time.time()
    if play_time is not None:
        return end_time - start_time    #플레이 시간 반환
    else:
        return None


def main():

    players = []    #각 플레이어의 기록을 저장할 리스트

    while True:
        player_name = input("What's your name? : ")
        print(f"Welcome, {player_name}!")

        while True:
            start_answer = input(f"{player_name}, would you like to start? (Y/N): ").strip().lower()
    
            if start_answer == "y":
                play_time = get_play_time()
                if play_time is not None:
                    players.append((player_name, play_time))
                    print(f"게임 플레이 시간: {play_time:.2f} 초")
                break
            elif start_answer == "n":
                print("Alright, see you next time.")
                break
            else:
                print("Invalid input. Please enter Y or N.")
    
        another_game = input("Would you like to play again? (Y/N): ").strip().lower()
        if another_game!= "y":
            break
        

#등수 매기기
    sorted_players = sorted(players, key=lambda x: x[1])    #플레이 시간 순으로 정렬

#결과 출력
    print("\n게임 결과:")
    for rank, (name, time) in enumerate(sorted_players, start=1):
        print(f"{rank}. {name}: {time:.2f} 초")


if __name__ == "__main__":
    main()
