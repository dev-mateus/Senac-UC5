from tkinter import *
root = Tk()
root.config(bg='blue')

fr1 = Frame(root)
fr2 = Frame(root)

lb1 = Label(fr1, text='Nome:', font='Arial 16 bold', anchor=E)
lb2 = Label(fr1, text='Sobrenome:', font='Arial 16 bold', anchor=E)
en1 = Entry(fr1, font='Arial 16 bold')
en2 = Entry(fr1, font='Arial 16 bold')
lb3 = Label(fr1, text='Sexo:', font='Arial 16 bold',  anchor=E)
cb1 = Checkbutton(fr1, text='Masculino', font='Arial 16 bold')
cb2 = Checkbutton(fr1, text='Feminino', font='Arial 16 bold')

fr1.grid(row=0, column=0)
fr2.grid(row=1, column=0)

lb1.grid(row=0, column=0, sticky=EW)
lb2.grid(row=1, column=0, sticky=EW)
en1.grid(row=0, column=1, columnspan=2)
en2.grid(row=1, column=1, columnspan=2)
lb3.grid(row=2, column=0, sticky=EW)
cb1.grid(row=2, column=1)
cb2.grid(row=2, column=2)

root.mainloop()