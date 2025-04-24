import random

# 宝の位置を決める（リストの中のインデックス）
map_size = 5
treasure_map = ["空き地"] * map_size
treasure_location = random.randint(0, map_size - 1)
treasure_map[treasure_location] = "宝！"

# プレイヤーにヒントを与えて選ばせる
print("=== 宝探しゲーム ===")
print(f"0から{map_size - 1}の中に宝が隠されているよ！")

try:
    guess = int(input("どこを掘る？数字を入力してね："))
    
    if 0 <= guess < map_size:
        if treasure_map[guess] == "宝！":
            print("おめでとう！宝を見つけた！🎉")
        else:
            print("残念！そこには何もなかった…😢")
    else:
        print("範囲外だよ！0から", map_size - 1, "の間で選んでね。")
except ValueError:
    print("数字を入力してね！")
