def treasure_game():
    line1 = ["0", "0", "0"]
    line2 = ["0", "0", "0"]
    line3 = ["0", "0", "0"]
    
    map = [line1, line2, line3]
    print("Hining your treasure! X marks tje spot")
    postion = map(int, input("좌표를 입력하세요").split()) #1, 3
    x = postion[0]
    y = postion[1]
    map[y-1][x-1] = "x"
    print(f"{line1}\n{line2}\n{line3}")

treasure_game()
