# calculadora simples
from tkinter import *


# back-end
def somar():
    soma = int(en1.get()) + int(en2.get())
    lb2['text'] = soma


# window
root = Tk()

# widget
lb1 = Label(root, text='Soma de dois números!')
en1 = Entry(root)
en2 = Entry(root)
bt1 = Button(root, text='Soma', command=somar)
lb2 = Label(root, text='Resultado!')

# layout
lb1.pack()
en1.pack()
en2.pack()
bt1.pack()
lb2.pack()

# run
root.mainloop()
