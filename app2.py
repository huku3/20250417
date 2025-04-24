import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO


# # 🐈️を表示させる関数
# def cat_button():
#     img = Image.open("cat_1.jpg")
#     img_tk = ImageTk.PhotoImage(img)

#     image_label.config(image=img_tk)
#     image_label.image = img_tk


# 画像を削除する関数
def clear():
    image_label.config(image=None)
    image_label.image = None


# catapiで猫の画像を作成する関数
def get_cat_image():
    url = "https://api.thecatapi.com/v1/images/search"
    response = requests.get(url)
    # print(response)
    # json形式に変換
    res = response.json()
    # 画像のURLを取得
    cat_url = res[0]["url"]
    # 画像のURLをリクエストして結果を変数に保存
    cat_response = requests.get(cat_url)
    # バイナリ形式からメモリ上でファイルのようにデータを扱えるようにしています
    cat_image = BytesIO(cat_response.content)
    img = Image.open(cat_image)
    # 画像をリサイズ
    img = img.resize((800, 600))
    img.thumbnail((800, 600))
    img_tk = ImageTk.PhotoImage(img)

    image_label.config(image=img_tk)
    image_label.image = img_tk

# ウインドウを作成
root = tk.Tk()
root.title("Cat-viewer")
root.geometry("1000x800")

# ボタン作成
button = tk.Button(root, text="猫ちゃんを表示する", command=get_cat_image)
button.pack(pady=50)

# 画像を削除するボタン作成
button2 = tk.Button(root, text="clear", command=clear)
button2.pack()

# 画像を表示するラベル作成
image_label = tk.Label(root)
image_label.pack()

root.mainloop()

# 猫の画像を削除する関数作成からつづき2
