# label interativo
from tkinter import *


# back-end

def diminuir():
    if int(lb1['text']) > -10:
        lb1['text'] = int(lb1['text']) - 1
    else:
        pass


def aumentar():
    if int(lb1['text']) < 10:
        lb1['text'] = int(lb1['text']) + 1
    else:
        pass


# janela
root = Tk()

# widgets
lb1 = Label(root, text='0', padx=20, pady=10, width=2)
bt1 = Button(root, text='-', command=diminuir, padx=10, pady=10, width=2)
bt2 = Button(root, text='+', command=aumentar, padx=10, pady=10, width=2)

# layout
bt1.grid(row=0, column=0)
lb1.grid(row=0, column=1)
bt2.grid(row=0, column=2)

# executa
root.mainloop()
