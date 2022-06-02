# importar a biblioteca tkinter
from tkinter import *

# criar uma janela com o nome 'root'
root = Tk()

# criar os widgets 'Label, Button e Entry' na janela 'root'
# criar um Label com o nome lb1 e adicionar o texto 'Label 1' no label
# o parâmetro bg declara a cor de fundo do Label e o fg a cor da fonte
lb1 = Label(root, text='Label 1', bg='Red', fg='white')
# criar um Label com o nome lb2 e adicionar o texto 'Label 1' no label
lb2 = Label(root, text='Label 2', bg='blue', fg='white')
# criar um Label com o nome lb3 e adicionar o texto 'Label 1' no label
lb3 = Label(root, text='Label 3', bg='yellow', fg='black')
# criar um Label com o nome lb4 e adicionar o texto 'Label 1' no label
lb4 = Label(root, text='Label 4', bg='green', fg='white')
# criar um Label com o nome lb5 e adicionar o texto 'Label 1' no label
lb5 = Label(root, text='Label 5', bg='pink', fg='black')


# Organizar os widgets criados com o gerenciador de pacote pack().
# O gerenciador pack() organiza os widgets através do parâmetro 'side',
# e empilha por ordem de forma ordenada os widgets através da posição
# declarada no side 'LEFT, RIGHT, TOP, BOTTOM, TOP'.
lb1.pack(side=LEFT)
lb2.pack(side=RIGHT)
lb3.pack(side=TOP)
lb4.pack(side=BOTTOM)
lb5.pack(side=TOP)

# executar a janela criada 'root' com a função mainloop()
root.mainloop()
