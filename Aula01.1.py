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
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

# widgets
lb1 = Label(root, text='0', padx=20, pady=10, width=3)
bt1 = Button(root, text='-', command=diminuir, padx=10, pady=10, width=3)
bt2 = Button(root, text='+', command=aumentar, padx=10, pady=10, width=3)

# layout
bt1.grid(row=0, column=0, sticky=NSEW)
lb1.grid(row=0, column=1, sticky=NSEW)
bt2.grid(row=0, column=2, sticky=NSEW)

# executa
root.mainloop()
