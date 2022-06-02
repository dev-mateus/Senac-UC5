# importar a biblioteca tkinter
from tkinter import *

# criar uma janela com o nome 'root'
root = Tk()
# o comando grid_rowconfigure torna a linha 0 responsiva
root.grid_rowconfigure(0, weight=1)
# o comando grid_rowconfigure torna a linha 1 responsiva
root.grid_rowconfigure(1, weight=1)
# o comando grid_columnconfigure torna a coluna 0 responsiva
root.grid_columnconfigure(0, weight=1)
# o comando grid_columnconfigure torna a coluna 1 responsiva
root.grid_columnconfigure(1, weight=1)


# Criar os widgets 'Label, Button e Entry' na janela 'root'
# o parâmetro bg declara a cor de fundo do Label e o fg a cor da fonte
# o parâmetro font define a família da fonte, o tamanho e o tipo.
# Criar um Label com o nome lb1 e adicionar o texto 'Label 1' no label
lb1 = Label(root, text='Label 1', bg='Red', fg='white', font='Arial 26 bold')
# criar um Label com o nome lb2 e adicionar o texto 'Label 2' no label
lb2 = Label(root, text='Label 2', bg='blue', fg='white', font='Arial 26 italic')
# criar um Label com o nome lb3 e adicionar o texto 'Label 3' no label
lb3 = Label(root, text='Label 3', bg='yellow', fg='black', font='Arial 26 bold')
# criar um Label com o nome lb4 e adicionar o texto 'Label 4' no label
lb4 = Label(root, text='Label 4', bg='green', fg='white', font='Arial 26 italic')
# criar um Label com o nome lb5 e adicionar o texto 'Label 5' no label
lb5 = Label(root, text='Label 5', bg='pink', fg='black', font='Arial 26 bold')
# criar um Label com o nome lb5 e adicionar o texto 'Label 6' no label
lb6 = Label(root, text='Label 6', bg='purple', fg='white', font='Arial 26 bold')

# Organizar os widgets criados com o gerenciador de pacote pack().
# O gerenciador grid() organiza os widgets através da posição row e column declarada.
# O comando sticky, estica o label em todas as direções NSEW
lb1.grid(row=0, column=0, sticky=NSEW)
lb2.grid(row=0, column=1, sticky=NSEW)
lb3.grid(row=1, column=0, sticky=NSEW)
lb4.grid(row=1, column=1, sticky=NSEW)
# o comando columnspan mescla a coluna 0 e 1 e mantém o label no centro dessa célula mesclada
# o comando sticky, estica o label de leste (E) a oeste (W)
lb5.grid(row=2, column=0, columnspan=2, sticky=EW)
# o comando rowspan mescla a linha 0 e 1 e mantém o label no centro dessa célula mesclada
# o comando sticky, estica o label de norte (N) a sul (S)
lb6.grid(row=0, column=2, rowspan=2, sticky=NS)

# executar a janela criada 'root' com a função mainloop()
root.mainloop()
