# importar a biblioteca tkinter
from tkinter import *


def ola():
    # o parâmetro 'text' do Label lb1 é alterado pela entrada de en1 usando a função get()
    lb1['text'] = en1.get()


# criar uma janela com o nome 'root'
root = Tk()
root.config(bg='blue') # cor de fundo da janela
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_columnconfigure(0, weight=1)

lb1 = Label(root, text='Olá Mundo!', font='Arial 26 bold', fg='yellow', bg='blue')
en1 = Entry(root, font='Arial 26', bg='yellow', fg='blue')
bt1 = Button(root, text='Clique aqui!', font='Arial 26',
             fg='yellow',
             bg='blue',
             activebackground='blue', # cor do botão quando o mouse está em cima do botão
             activeforeground='red', # cor da fonte quando o mouse está em cima do botão
             command=ola # command chama a função olá
             )

lb1.grid(sticky=NSEW)
en1.grid(sticky=NSEW)
bt1.grid(sticky=NSEW)

# executar a janela criada 'root' com a função mainloop()
root.mainloop()
