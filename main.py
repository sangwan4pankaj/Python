## Signup

from tkinter import *

from PIL import ImageTk, Image


class Signup:
    def __init__(self, root):
        self.root = root
        self.root.title = ("Signup Page")
        self.root.geometry("500x400+10+10")
        img = Image.open('C:\\Users\\Admin\\bg.jpg')
        bg = ImageTk.PhotoImage(img)

        # Add image
        imgLb = Label(self.root, image=bg)
        imgLb.place(x=0, y=0)


root = Tk()

signup_ob = Signup(root)

root.mainloop()