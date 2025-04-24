import requests
import os
import tkinter as tk
from dotenv import load_dotenv


load_dotenv()
api_key = os.getenv("API_KEY")
# print(api_key)
# city = input("都市名を入力: ")


def get_weather():
    city = city_entry.get()
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=ja"

    response = requests.get(url)

    # print(response)
    # print(response.text)
    if response.status_code == 200:
        data = response.json()
        # 気温
        temp = data["main"]["temp"]
        # 天気
        weather = data["weather"][0]["description"]

        # print(f"{city}の天気: {weather}\n気温: {temp}℃")
        result_label.config(text=f"{city}の天気: {weather}\n気温: {temp}℃")
    else:
        # print(f"エラー: {response.text}")
        result_label.config(text="天気情報が取得できませんでした")


# 画面を作成
root = tk.Tk()
root.title("天気情報アプリ")
root.geometry("500x500")

# 都市名のラベルと入力フィールド
tk.Label(root, text="都市名を入力: ").pack()
city_entry = tk.Entry(root)
city_entry.pack()

# ボタン作成
tk.Button(root, text="天気を取得", command=get_weather).pack()

# 結果を表示するラベル
result_label = tk.Label(root, text="")
result_label.pack()


# 画面を表示
root.mainloop()
