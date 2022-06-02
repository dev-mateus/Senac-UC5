# importar a biblioteca tkinter
from tkinter import *

# criar uma janela com o nome 'root'
root = Tk()

# criar os widgets 'Label, Button e Entry' na janela 'root'
# criar um Label com o nome lb1 e adicionar o texto 'Label 1' no label
lb1 = Label(root, text='Label 1')

# criar um botão com o nome bt1 e adicionar o texto 'Botão 1' no botão
bt1 = Button(root, text='Botão 1')

# criar uma caixa de texto com o nome en1
en1 = Entry(root)

# organizar os widgets criados com o gerenciador de pacote pack().
lb1.pack()
bt1.pack()
en1.pack()

# executar a janela criada 'root' com a função mainloop()
root.mainloop()
