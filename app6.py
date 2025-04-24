import pygame
import time

# pygameの初期化
pygame.init()

# 音をセット
sound_files = {
    "a": "do.wav",  # ド
    "s": "re.wav",  # レ
    "d": "mi.wav",  # ミ
    "f": "fa.wav",  # ファ
    "g": "so.wav",  # ソ
    "h": "la.wav",  # ラ
    "j": "si.wav",  # シ
    "k": "do2.wav", # ド
}

# 音を読み込む
sounds = {key: pygame.mixer.Sound(file) for key, file in sound_files.items()}

# キーボード操作を待つ
print("キー 'a'～'j' を押してドレミファソラシドを演奏しよう！")

while True:
    key = input("押したキーを入力 ('q'で終了): ").lower()
    
    # 終了条件
    if key == "q":
        pygame.quit()
        break

    # キーに対応した音を鳴らす
    if key in sounds:
        sounds[key].play()
        time.sleep(1)  # 音を鳴らして少し待つ
    else:
        print("無効なキーです。'a'～'j'で演奏してください。")
