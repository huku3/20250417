import pygame
import sys

# Pygameの初期化
pygame.init()

# 画面サイズ
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pygameでキャラクターを動かす")

# キャラクターの読み込みとサイズ調整
character_image = pygame.image.load("img.jpg")
character_image = pygame.transform.scale(character_image, (100, 100))  # 適切なサイズに変更

# キャラクターの初期位置
# 画面の中央
character_x, character_y = SCREEN_WIDTH / 2 - 50, SCREEN_HEIGHT / 2 - 50

# キャラクターの移動速度
character_speed = 0.5

# 色の設定
background_color = (255, 255, 255)  # 白色

# ゲームループ
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # キーの状態を取得
    keys = pygame.key.get_pressed()

    # 矢印キーでの移動
    if keys[pygame.K_LEFT]:
        character_x -= character_speed
    
    if keys[pygame.K_RIGHT]:
        character_x += character_speed

    if keys[pygame.K_UP]:
        character_y -= character_speed

    if keys[pygame.K_DOWN]:
        character_y += character_speed
    
    # 画面外に出ないように制御
    character_x = max(0, min(character_x, SCREEN_WIDTH - character_image.get_width()))
    character_y = max(0, min(character_y, SCREEN_HEIGHT - character_image.get_height()))

    # 背景色の設定
    screen.fill(background_color)

    # キャラクターの描画
    screen.blit(character_image, (character_x, character_y))

    pygame.display.flip()
