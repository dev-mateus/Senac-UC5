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

# caixa de entrada
etr1 = Entry(janela)
etr1.place(x=100, y=50, width=200)

etr2 = Entry(janela)
etr2.place(x=100, y=75, width=200)

# botões
bt1 = Button(janela, text='+')
bt1.place(x=100, y=20, width=50)
bt1['command'] = soma

bt2 = Button(janela, text='-')
bt2.place(x=150, y=20, width=50)
bt2['command'] = subtracao

bt3 = Button(janela, text='*')
bt3.place(x=200, y=20, width=50)
bt3['command'] = multiplicacao

bt4 = Button(janela, text='/')
bt4.place(x=250, y=20, width=50)
bt4['command'] = divisao

# label
lb1 = Label(janela, text='Resultado!')
lb1.place(x=100, y=100, width=200)

# execução da instancia
janela.mainloop()
