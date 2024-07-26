#open 함수
import os

file_path = "새 파일2.txt"

if os.path.exists(file_path):
    os.remove(file_path)
    print(f"{file_path} 파일이 삭제되었습니다.")
else:
    print(f"{file_path} 파일을 찾을 수 없습니다.")
    