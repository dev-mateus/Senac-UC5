# Aula 01 será apresentado os elementos básicos de uma GUI
# -*- coding: utf-8 -*-
from tkinter import *


# BACK-END
def imprimir():
    lb2['text'] = ent1.get()
    print(ent1.get())


def click(msg):
    lb2['text'] = msg
    print(msg)


# ELEMENTOS:
# 1) WINDOW
root = Tk()
root.title('App GUI')
root.geometry('200x130')

# 2) FRAME

# 3) WIDGET
lb1 = Label(root, text='Digite aqui:')
lb2 = Label(root)
ent1 = Entry(root)
# btn1 = Button(root, text='Click aqui!', command=imprimir)
btn1 = Button(root, text='Click aqui!', command=lambda: click(ent1.get()))
btn2 = Button(root, text='Sair', command=quit)

# 4) LAYOUT
# 4.1) PLACE

lb1.place(x=10, y=10)
ent1.place(x=10, y=30)
btn1.place(x=10, y=60)
btn2.place(x=110, y=60)
lb2.place(x=10, y=100)

# 4.1) PACK
'''
lb1.pack()
ent1.pack()
btn1.pack(fill='both', expand=1, pady=5, padx=5)
btn2.pack(fill='both', expand=1, pady=5, padx=5)
lb2.pack()
'''
# 4.3) GRID
'''
lb1.grid(row=0, column=0)
ent1.grid(row=1, column=0)
btn1.grid(row=2, column=0)
btn2.grid(row=3, column=0)
lb2.grid(row=4, column=0)
'''
# EXECUTA O WINDOW
root.mainloop()
