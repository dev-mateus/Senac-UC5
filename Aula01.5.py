from tkinter import *

janela = Tk()
janela.title('Calculadora')
janela.geometry('200x250')

ent1 = Entry(janela)
ent1.grid(row=0, column=0, columnspan=5, sticky=W+E)

lb1 = Label(janela)
lb1.grid(row=1, column=0, columnspan=5)

bt7 = Button(text='7', width=2, height=1)
bt7.grid(row=2, column=0)

bt8 = Button(text='8', width=2, height=1)
bt8.grid(row=2, column=1)

bt9 = Button(text='9', width=2, height=1)
bt9.grid(row=2, column=2)

bt4 = Button(text='4', width=2, height=1)
bt4.grid(row=3, column=0)

bt5 = Button(text='5', width=2, height=1)
bt5.grid(row=3, column=1)

bt6 = Button(text='6', width=2, height=1)
bt6.grid(row=3, column=2)

bt1 = Button(text='1', width=2, height=1)
bt1.grid(row=4, column=0)

bt2 = Button(text='2', width=2, height=1)
bt2.grid(row=4, column=1)

bt3 = Button(text='3', width=2, height=1)
bt3.grid(row=4, column=2)

bt0 = Button(text='0', width=2, height=1)
bt0.grid(row=5, column=0)

bt10 = Button(text='=', bg='gray', width=2, height=1)
bt10.grid(row=5, column=1)

bt11 = Button(text='*', width=2, height=1)
bt11.grid(row=2, column=4)

bt12 = Button(text='/', width=2, height=1)
bt12.grid(row=3, column=4)

bt13 = Button(text='+', width=2, height=1)
bt13.grid(row=4, column=4)

bt14 = Button(text='-', width=2, height=1)
bt14.grid(row=5, column=4)

bt14 = Button(text='.', width=2, height=1)
bt14.grid(row=5, column=2)

janela.mainloop()
