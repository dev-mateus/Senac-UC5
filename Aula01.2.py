from tkinter import *


# back-end
def imc():
    peso = float(in1.get())
    altura = float(in2.get())
    resultado = peso/(altura*altura)
    lb3['text'] = resultado


# window
root = Tk()

# widgets
lb1 = Label(root, text='Peso:')
lb2 = Label(root, text='Altura:')
lb3 = Label(root)
in1 = Entry(root)
in2 = Entry(root)
bt1 = Button(root, text='IMC', command=imc)

# layout
lb1.grid(row=0, column=0)
lb2.grid(row=1, column=0)
in1.grid(row=0, column=1)
in2.grid(row=1, column=1)
bt1.grid(row=2, column=0)
lb3.grid(row=2, column=1)

# run
root.mainloop()
