import tkinter as tk
def show_info():
    name_label.config(text="Abigail Swinborne")
    address.config(text="1111 11th Street Hobbiton, Shire 11111")
def quit_gui():
    root.destroy()

root = tk.Tk()
root.title("Program 2")

info_label = tk.Label(root, text="")
info_label.pack()

show_info = tk.Button(root, text="Show Info", command=show_info)
show_info.pack()

name_label = tk.Label(root, text="Name")
name_label.pack()

address = tk.Label(root, text="Address")
address.pack()

quit_button = tk.Button(root, text="Quit", command=quit_gui)
quit_button.pack()

root.mainloop()