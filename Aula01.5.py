# calculadora
from tkinter import *

root = Tk()

fr1 = Frame(root)
fr2 = Frame(root)

lb1 = Label(fr1)
en1 = Entry(fr1)

bt1 = Button(fr2, text='1')
bt2 = Button(fr2, text='2')
bt3 = Button(fr2, text='3')
bt4 = Button(fr2, text='4')
bt5 = Button(fr2, text='5')
bt6 = Button(fr2, text='6')
bt7 = Button(fr2, text='7')
bt8 = Button(fr2, text='8')
bt9 = Button(fr2, text='9')

fr1.pack()
fr2.pack()

lb1.pack()
en1.pack()

bt1.grid(row=0, column=0)
bt2.grid(row=0, column=1)
bt3.grid(row=0, column=2)
bt4.grid(row=1, column=0)
bt5.grid(row=1, column=1)
bt6.grid(row=1, column=2)
bt7.grid(row=2, column=0)
bt8.grid(row=2, column=1)
bt9.grid(row=2, column=2)

root.mainloop()
