# main.py

from game import ts_game, Player, save_player_info, load_player_info, Timer
from assets.banner import print_banner
import os

def main():
    print_banner()
    print("Welcome to Treasure Island.")
    print("Your mission is to find the treasure.")

    players = []    # 각 플레이어의 기록을 저장할 리스트
    
    # main.py 파일이 있는 디렉토리 경로 가져오기
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "player_data.txt")

    players.extend(load_player_info(file_path))  # 파일에서 기존 플레이어 정보를 불러옴

    while True:
        player_name = input("What's your name? : ").strip()
        if not player_name:
            print("Name cannot be empty. Please enter your name.")
            continue

        print(f"Welcome, {player_name}!")
        player = Player(player_name)
        timer = Timer()

        while True:
            start_answer = input(f"{player_name}, would you like to start? (Y/N): ").strip().lower()
    
            if start_answer == "y":
                timer.start()
                game_result = ts_game()
                if game_result:
                    play_time = timer.stop()
                    player.set_play_time(play_time)
                    players.append(player)
                    print(f"게임 플레이 시간: {play_time:.2f} 초")
                break
            elif start_answer == "n":
                print("Alright, see you next time.")
                break
            else:
                print("Invalid input. Please enter Y or N.")
    
        another_game = input("Would you like to play again? (Y/N): ").strip().lower()
        if another_game != "y":
            break
        
    # 등수 매기기
    sorted_players = sorted(players, key=lambda x: x.play_time)  # 플레이 시간 순으로 정렬

    # 결과 출력
    print("\n게임 결과:")
    for rank, player in enumerate(sorted_players, start=1):
        print(f"{rank}. {player.name}: {player.play_time:.2f} 초")

    # 플레이어 정보를 파일에 저장
    save_player_info(file_path, sorted_players)

if __name__ == "__main__":
    main()
