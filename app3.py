import tkinter as tk
from tkinter import ttk
import sqlite3

# --- DB準備 ---
conn = sqlite3.connect("books.db")
c = conn.cursor()
c.execute("""
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        author TEXT,
        review TEXT
    )
""")
conn.commit()

# --- 本の登録処理 ---
def add_book():
    title = title_entry.get()
    author = author_entry.get()
    review = review_entry.get("1.0", tk.END)

    if title and author:
        c.execute("INSERT INTO books (title, author, review) VALUES (?, ?, ?)",
                  (title, author, review))
        conn.commit()
        title_entry.delete(0, tk.END)
        author_entry.delete(0, tk.END)
        review_entry.delete("1.0", tk.END)
        show_books()
    else:
        result_label.config(text="タイトルと著者は必須です")

# --- 一覧表示処理 ---
def show_books():
    for row in tree.get_children():
        tree.delete(row)

    c.execute("SELECT title, author, review FROM books")
    for row in c.fetchall():
        tree.insert("", tk.END, values=row)

# --- UIの構築 ---
root = tk.Tk()
root.title("読書ログアプリ")
root.geometry("600x500")

tk.Label(root, text="タイトル").pack()
title_entry = tk.Entry(root, width=50)
title_entry.pack()

tk.Label(root, text="著者").pack()
author_entry = tk.Entry(root, width=50)
author_entry.pack()

tk.Label(root, text="感想").pack()
review_entry = tk.Text(root, height=4, width=50)
review_entry.pack()

tk.Button(root, text="登録", command=add_book).pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack()

# --- 一覧（Treeview）---
columns = ("タイトル", "著者", "感想")
tree = ttk.Treeview(root, columns=columns, show="headings", height=8)
for col in columns:
    tree.heading(col, text=col)
tree.pack()

# 最初に表示
show_books()

root.mainloop()
