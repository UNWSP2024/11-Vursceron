import tkinter as tk

def create_gui():
    root = tk.Tk()
    root.title("My Favorite Saying")
    favorite_saying = ('I have lived a thousand live, I have loved a thousand loves, I have walked on distant shores and seen the end of time because I read -George R.R. Martin')
    label = tk.Label(root, text=favorite_saying, padx=20, pady=20)
    label.pack()
    root.mainloop()
create_gui()

