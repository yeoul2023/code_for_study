import os
from .player import Player  
# '.player'의 . 은 현재 폴더를 나타냄
# 패키지 내부에서 모듈을 참조할때는 상대 임포트를 사용하는 것이 좋음

def save_player_info(file_path, players):
    with open(file_path, 'w') as f:
        for player in players:
            f.write(f"{player.name},{player.play_time}\n")
    print(f"플레이어 데이터가 {file_path} 경로에 저장되었습니다.")

def load_player_info(file_path):
    players = []
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            for line in f:
                name, play_time = line.strip().split(',')
                player = Player(name)
                player.set_play_time(float(play_time))
                players.append(player)
        print("플레이어 데이터를 읽어왔습니다.")
    else:
        print("플레이어 기록이 없습니다.")
        directory = os.path.dirname(file_path)
        if directory:
            os.makedirs(directory, exist_ok=True)
        open(file_path, 'w').close()  # 새로운 파일 생성

    return players