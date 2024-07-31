#game_logic.py
def ts_game():
    while True:
        first_case = input("left or right?: ").strip().lower()
        if first_case == "left":
            second_case = input("swim or wait?: ").strip().lower()
            if second_case == "wait":
                third_case = input("Which door? Red, Blue or Yellow: ").strip().lower()
                if third_case == "red":
                    print("Burned by fire. Game over.")
                    return None
                elif third_case == "blue":
                    print("Eaten by beasts. Game over.")
                    return None
                elif third_case == "yellow":
                    print("you win!!")
                    return True  # 게임 성공 반환
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
