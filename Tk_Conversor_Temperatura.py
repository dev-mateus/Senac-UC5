# conversão
from tkinter import *


# back-end
def converte():
    c = float(in1.get())
    f = c * 1.8 + 32
    lb2['text'] = f


# window
root = Tk()

# widgets
lb1 = Label(root, text='C°:')
lb2 = Label(root)
in1 = Entry(root)
bt1 = Button(root, text='Converte °F', command=converte)

# layout
lb1.grid(row=0, column=0)
lb2.grid(row=1, column=1)
in1.grid(row=0, column=1)
bt1.grid(row=1, column=0)

# run
root.mainloop()
