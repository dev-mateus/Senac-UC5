from tkinter import *


def soma():
    if str(etr1.get()).isnumeric() and str(etr2.get()).isnumeric():
        num1 = float(etr1.get())
        num2 = float(etr2.get())
        lb1['text'] = num1 + num2
    else:
        pass


def subtracao():
    if str(etr1.get()).isnumeric() and str(etr2.get()).isnumeric():
        num1 = float(etr1.get())
        num2 = float(etr2.get())
        lb1['text'] = num1 - num2
    else:
        pass


def multiplicacao():
    if str(etr1.get()).isnumeric() and str(etr2.get()).isnumeric():
        num1 = float(etr1.get())
        num2 = float(etr2.get())
        lb1['text'] = num1 * num2
    else:
        pass


def divisao():
    if str(etr1.get()).isnumeric() and str(etr2.get()).isnumeric():
        num1 = float(etr1.get())
        num2 = float(etr2.get())
        lb1['text'] = num1 / num2
    else:
        pass


# janela principal
janela = Tk()
janela.geometry('400x140')
janela.title('CalcPy')

# widgets
fr1 = Frame(janela)
etr1 = Entry(janela)
etr2 = Entry(janela)
bt1 = Button(fr1, text='+', command=soma, width=2)
bt2 = Button(fr1, text='-', command=subtracao, width=2)
bt3 = Button(fr1, text='*', command=multiplicacao, width=2)
bt4 = Button(fr1, text='/', command=divisao, width=2)
lb1 = Label(janela, text='Resultado!')

# layout
bt1.pack(side=LEFT)
bt2.pack(side=LEFT)
bt3.pack(side=LEFT)
bt4.pack(side=LEFT)
etr1.pack()
etr2.pack()
fr1.pack()
lb1.pack()

# execução da instancia
janela.mainloop()
