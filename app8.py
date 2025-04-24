import pygame
import time

pygame.init()

sound_files = {
    "a": "do.wav",   # ド
    "s": "re.wav",   # レ
    "d": "mi.wav",   # ミ
    "f": "fa.wav",   # ファ
    "g": "so.wav",   # ソ
    "h": "la.wav",   # ラ
    "j": "si.wav",   # シ
}

# sounds = {key: pygame.mixer.Sound(file) for key, file in sound_files.items()}
sounds = {}
for key, file in sound_files.items():
    sounds[key] = pygame.mixer.Sound(file)

# きらきら星のメロディ（キー対応）
melody = [
    "a", "a", "g", "g", "h", "h", "g",      # ドドソソララソ
    "f", "f", "d", "d", "s", "s", "a",      # ファファミミレレド
    "g", "g", "f", "f", "d", "d", "s",      # ソソファファミミレ
    "g", "g", "f", "f", "d", "d", "s",      # ソソファファミミレ
    "a", "a", "g", "g", "h", "h", "g",      # ドドソソララソ
    "f", "f", "d", "d", "s", "s", "a"       # ファファミミレレド
]

# melody = [
#     "a", "s", "d", "f", "d", "s", "d",
#     "g", "h", "h", "g", "d", "s", "a"
# ]

# melody = [
#     "a", "a", "s", "a", "f", "d",
#     "a", "a", "s", "a", "g", "f"
# ]

for note in melody:
    sounds[note].play()
    time.sleep(0.5)

pygame.quit()
