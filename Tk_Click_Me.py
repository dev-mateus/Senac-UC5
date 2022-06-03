from tkinter import *
import tkinter as tk


def click_me(msg):
    lb1['text'] = msg


def clear():
    en1.delete(0, END)
    lb1['text'] = 'Olá mundo de novo!!!'


root = Tk()

lb1 = Label(root, text='Olá mundo de novo!!!')
en1 = Entry(root)
bt1 = Button(root, text='click me!', command=lambda: click_me(en1.get()))
bt2 = Button(root, text='clear!', command=lambda: clear())

lb1.pack()
en1.pack()
bt1.pack()
bt2.pack()

root.mainloop()
