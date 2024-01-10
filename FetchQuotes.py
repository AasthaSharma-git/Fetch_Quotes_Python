import tkinter as tk
import requests
import customtkinter as ctk


def fetch_quote(category=None, author=None):
    url = "https://api.quotable.io/random"

    if category:
        url += f"?tags={category}"
    elif author:
        url += f"?author={author}"

    response = requests.get(url)
    if response.status_code == 200:
        quote_data = response.json()
        quote = f'"{quote_data["content"]}" - {quote_data["author"]}'
        result_text.config(text=quote)
    else:
        result_text.config(text="Error fetching quote")

# Tkinter GUI setup
root = tk.Tk()
root.title("Quote Generator")

generate_button = tk.Button(root, text="Generate Random Quote", command=fetch_quote)
generate_button.pack(pady=10)

category_input=ctk.CTkEntry(root,placeholder_text='Enter category')
category_input.pack(pady=10)

generate_category_button = tk.Button(root, text="Generate Quote by Category", command=lambda: fetch_quote(category=category_input.get()))
generate_category_button.pack(pady=10)

author_input=ctk.CTkEntry(root,placeholder_text='Enter author')
author_input.pack(pady=10)

generate_author_button = tk.Button(root, text="Generate Quote by Author", command=lambda: fetch_quote(author=author_input.get()))
generate_author_button.pack(pady=10)

result_text = tk.Label(root, text="", wraplength=400)
result_text.pack(pady=10)

root.mainloop()
