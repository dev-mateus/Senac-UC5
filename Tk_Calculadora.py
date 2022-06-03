from tkinter import *


def entrada(valor):
    if lb1['text'] == 'Conta Invalida':
        lb1['text'] = ''
        lb1['fg'] = '#a07000'
    else:
        lb1['fg'] = '#a07000'
        lb1['text'] += valor


def saida():
    ultimo_digito = lb1['text'][len(lb1['text']) - 1]
    if ultimo_digito != '+' and ultimo_digito != '-' and ultimo_digito != '*' and ultimo_digito != '/':
        res = eval(lb1['text'])
        lb1['text'] = str(res)
        lb1['fg'] = '#27990d'
    else:
        lb1['text'] = 'Conta Invalida'
        lb1['fg'] = '#aa0303'


def limpa():
    lb1['text'] = ''


janela = Tk()
janela.title('Calculadora')
janela.geometry('400x500')
janela.bind('<Escape>', lambda event: limpa())
janela.bind('<Return>', lambda event: saida())

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
lb1 = Label(janela, font='Verdana 30', bg='#414249', fg='#a07000')
bt7 = Button(janela, text='7', width=2, height=1, font='Verdana 26', command=lambda: entrada('7'))
bt8 = Button(janela, text='8', width=2, height=1, font='Verdana 26', command=lambda: entrada('8'))
bt9 = Button(janela, text='9', width=2, height=1, font='Verdana 26', command=lambda: entrada('9'))
bt4 = Button(janela, text='4', width=2, height=1, font='Verdana 26', command=lambda: entrada('4'))
bt5 = Button(janela, text='5', width=2, height=1, font='Verdana 26', command=lambda: entrada('5'))
bt6 = Button(janela, text='6', width=2, height=1, font='Verdana 26', command=lambda: entrada('6'))
bt1 = Button(janela, text='1', width=2, height=1, font='Verdana 26', command=lambda: entrada('1'))
bt2 = Button(janela, text='2', width=2, height=1, font='Verdana 26', command=lambda: entrada('2'))
bt3 = Button(janela, text='3', width=2, height=1, font='Verdana 26', command=lambda: entrada('3'))
bt0 = Button(janela, text='0', width=2, height=1, font='Verdana 26', command=lambda: entrada('0'))
bt10 = Button(janela, text='=', bg='gray', width=2, height=1, font='Verdana 26', command=saida)
bt11 = Button(janela, text='*', width=2, height=1, font='Verdana 26', command=lambda: entrada('*'))
bt12 = Button(janela, text='/', width=2, height=1, font='Verdana 26', command=lambda: entrada('/'))
bt13 = Button(janela, text='+', width=2, height=1, font='Verdana 26', command=lambda: entrada('+'))
bt14 = Button(janela, text='-', width=2, height=1, font='Verdana 26', command=lambda: entrada('-'))
bt15 = Button(janela, text='.', width=2, height=1, font='Verdana 26', command=lambda: entrada('.'))

# layout
lb1.grid(row=0, column=0, columnspan=5, sticky=NSEW)
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
