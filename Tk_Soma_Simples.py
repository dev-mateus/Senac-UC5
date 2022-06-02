from tkinter import *


def soma():
    # método isnumeric() verifica se en1 e en2 são entradas numéricas
    # método replace retira o ponto de um número decimal para que método isnumeric() entenda a entrada como número
    if en1.get().replace('.', '').isnumeric() and en2.get().replace('.', '').isnumeric():
        # o método float() converte as entradas en1 e en2 de string para float
        lb1['text'] = float(en1.get()) + float(en2.get())
    else:
        lb1['text'] = 'Entrada Invalida!'


root = Tk()

en1 = Entry(root, font='Arial 26')
en2 = Entry(root, font='Arial 26')
bt1 = Button(root, text='Soma', font='Arial 26', command=soma)
lb1 = Label(root, text='Resultado', font='Arial 26')

en1.grid()
en2.grid()
bt1.grid()
lb1.grid()

root.mainloop()
