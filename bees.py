import requests
import customtkinter
from tkinter import *
from PIL import Image, ImageTk
import random


def get_images():
    count = 1
    while count <= 5:
        with open(r'images.txt', 'r') as f:
            content = f.readlines()
            url = content[random.randint(1, 8471)].replace("\n", "")
        res = requests.get(url, stream=True)
        if res.status_code == 200:
            with open(f"images/bee{count}.jpg", 'wb') as f:
                f.write(res.content)
        count += 1


def gui():
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")
    global root
    root = customtkinter.CTk()
    root.title("Bees")
    root.configure(bg="yellow")
    root.resizable(False, False)
    frame = customtkinter.CTkFrame(
        root, 400, 150, border_color="#EB1F1F", bg_color="yellow")
    customtkinter.CTkLabel(frame, 400, 150, text="BEES", font=(
        "italic", 160), text_color="yellow").pack(anchor="center", side="top")
    frame.pack()
    image = ImageTk.PhotoImage(i[0])
    global imlabel
    imlabel = customtkinter.CTkLabel(root, image=image, text="")
    frame2 = customtkinter.CTkFrame(root, 400, 100)

    def previos():
        if i["count"] == 0:
            pass
        else:
            i["count"] -= 1
            root.pack_slaves()[2].destroy()
            customtkinter.CTkLabel(root, image=ImageTk.PhotoImage(
                i[i["count"]]), text="").pack()

    def next():
        if i["count"] == 4:
            pass
        else:
            i["count"] += 1
            root.pack_slaves()[2].destroy()
            customtkinter.CTkLabel(root, image=ImageTk.PhotoImage(
                i[i["count"]]), text="").pack()

    def exit():
        root.pack_slaves()[2].destroy()
        root.destroy()

    def new_images():
        get_images()
        i[0] = Image.open("images/bee1.jpg")
        i[1] = Image.open("images/bee2.jpg")
        i[2] = Image.open("images/bee3.jpg")
        i[3] = Image.open("images/bee4.jpg")
        i[4] = Image.open("images/bee5.jpg")
        i["count"] = 0
        root.pack_slaves()[2].destroy()
        customtkinter.CTkLabel(root, image=ImageTk.PhotoImage(
            i[i["count"]]), text="").pack()
        print(root.pack_slaves())
        print(len(root.pack_slaves()))
    button1 = customtkinter.CTkButton(
        frame2, 150, command=previos, text="previous picture").pack(side=RIGHT, padx=32)
    button2 = customtkinter.CTkButton(
        frame2, 150, command=next, text="next picture").pack(side=LEFT, padx=32)
    button3 = customtkinter.CTkButton(
        frame2, text="exit", command=exit).pack(side=BOTTOM, pady=10)
    button4 = customtkinter.CTkButton(
        frame2, text="generate new images", command=new_images).pack(side=TOP)
    frame2.pack()
    imlabel.pack()
    root.mainloop()


get_images()
i = {}
i[0] = Image.open("images/bee1.jpg")
i[1] = Image.open("images/bee2.jpg")
i[2] = Image.open("images/bee3.jpg")
i[3] = Image.open("images/bee4.jpg")
i[4] = Image.open("images/bee5.jpg")
i["count"] = 0

gui()
