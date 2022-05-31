from tkinter import *


def resultado(valor):
    lb1['text'] += valor


def saida():
    lb1['text'] = eval(lb1['text'])


janela = Tk()
janela.title('Calculadora')
janela.geometry('200x250')

janela.grid_rowconfigure(0, weight=1, minsize=50)
janela.grid_rowconfigure(1, weight=1, minsize=50)
janela.grid_rowconfigure(2, weight=1, minsize=50)
janela.grid_rowconfigure(3, weight=1, minsize=50)
janela.grid_rowconfigure(4, weight=1, minsize=50)

janela.grid_columnconfigure(0, weight=1, minsize=50)
janela.grid_columnconfigure(1, weight=1, minsize=50)
janela.grid_columnconfigure(2, weight=1, minsize=50)
janela.grid_columnconfigure(3, weight=1, minsize=50)

# widgets
lb1 = Label(janela)
bt7 = Button(text='7', width=2, height=1, command=lambda: resultado('7'))
bt8 = Button(text='8', width=2, height=1, command=lambda: resultado('8'))
bt9 = Button(text='9', width=2, height=1, command=lambda: resultado('9'))
bt4 = Button(text='4', width=2, height=1, command=lambda: resultado('4'))
bt5 = Button(text='5', width=2, height=1, command=lambda: resultado('5'))
bt6 = Button(text='6', width=2, height=1, command=lambda: resultado('6'))
bt1 = Button(text='1', width=2, height=1, command=lambda: resultado('1'))
bt2 = Button(text='2', width=2, height=1, command=lambda: resultado('2'))
bt3 = Button(text='3', width=2, height=1, command=lambda: resultado('3'))
bt0 = Button(text='0', width=2, height=1, command=lambda: resultado('0'))
bt10 = Button(text='=', bg='gray', width=2, height=1, command=saida)
bt11 = Button(text='*', width=2, height=1, command=lambda: resultado('*'))
bt12 = Button(text='/', width=2, height=1, command=lambda: resultado('/'))
bt13 = Button(text='+', width=2, height=1, command=lambda: resultado('+'))
bt14 = Button(text='-', width=2, height=1, command=lambda: resultado('-'))
bt15 = Button(text='.', width=2, height=1, command=lambda: resultado('.'))

# layout
lb1.grid(row=0, column=0, columnspan=5, sticky=EW)
bt7.grid(row=1, column=0, sticky=NSEW)
bt8.grid(row=1, column=1, sticky=NSEW)
bt9.grid(row=1, column=2, sticky=NSEW)
bt4.grid(row=2, column=0, sticky=NSEW)
bt5.grid(row=2, column=1, sticky=NSEW)
bt6.grid(row=2, column=2, sticky=NSEW)
bt1.grid(row=3, column=0, sticky=NSEW)
bt2.grid(row=3, column=1, sticky=NSEW)
bt3.grid(row=3, column=2, sticky=NSEW)
bt0.grid(row=4, column=0, sticky=NSEW)
bt10.grid(row=4, column=1, sticky=NSEW)
bt11.grid(row=1, column=3, sticky=NSEW)
bt12.grid(row=2, column=3, sticky=NSEW)
bt13.grid(row=3, column=3, sticky=NSEW)
bt14.grid(row=4, column=3, sticky=NSEW)
bt15.grid(row=4, column=2, sticky=NSEW)

janela.mainloop()
