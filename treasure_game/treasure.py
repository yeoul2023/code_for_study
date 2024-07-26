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
import os

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
        total_time = end_time - start_time
        return round(total_time, 2) #플레이 시간 반환
    else:
        return None

def save_player_info(file_path, players):
    """
    플레이어 정보를 텍스트 파일로 저장합니다.
    :param file_path: 저장할 파일 경로
    :param players: 플레이어 정보 리스트 (리스트의 각 요소는 (순위, 이름) 튜플)
    """
    with open(file_path, 'w') as f:
        for player_name, play_time in players:
            f.write(f"{player_name},{play_time}\n")
    print(f"플레이어 데이터가 {file_path} 경로에 저장되었습니다.")

def load_player_info(file_path):
    """
    텍스트 파일에서 플레이어 정보를 읽어옵니다.
    :param file_path: 읽어올 파일 경로
    :return: 플레이어 정보 리스트 (리스트의 각 요소는 (순위, 이름) 튜플)
    """
    players_data = []
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            for line in f:
                player_name, play_time = line.strip().split(',')
                players_data.append((player_name, float(play_time)))
        print("플레이어 데이터를 읽어왔습니다.")
    else:
        print("플레이어 기록이 없습니다.")
        directory = os.path.dirname(file_path)
        if directory:
            os.makedirs(directory, exist_ok=True)
        open(file_path, 'w').close()  # 새로운 파일 생성

    return players_data


def main():

    players = []    #각 플레이어의 기록을 저장할 리스트
    
    # treasure.py 파일이 있는 디렉토리 경로 가져오기
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "player_data.txt")

    players.extend(load_player_info(file_path)) # 파일에서 기존 플레이어 정보를 불러옴

    while True:
        player_name = input("What's your name? : ").strip()
        if not player_name:
            print("Name cannot be empty. Please enter your name.")
            continue

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



    # 플레이어 정보를 파일에 저장
    save_player_info(file_path, sorted_players)


if __name__ == "__main__":
    main()
