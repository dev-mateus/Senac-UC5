from tkinter import *


def imc():
    if en1.get().replace('.', '').isnumeric() and en2.get().replace('.', '').isnumeric():
        # método round formata a saída float para apresentar apenas 1 casas decimais depois da virgula
        lb3['text'] = round(float(en1.get()) / (float(en2.get()) * float(en2.get())), 1)
        # classificação de imc
        if lb3['text'] < 18.5:
            lb4['text'] = 'Abaixo do peso!'
            lb4['fg'] = 'blue'
        elif 18.5 <= lb3['text'] <= 24.9:
            lb4['text'] = 'Peso normal!'
            lb4['fg'] = 'green'
        elif 25 <= lb3['text'] <= 29.9:
            lb4['text'] = 'Sobrepeso!'
            lb4['fg'] = 'yellow'
        elif 30 <= lb3['text'] <= 34.9:
            lb4['text'] = 'Obesidade Grau 1!'
            lb4['fg'] = 'orange'
        elif 35 <= lb3['text'] <= 39.9:
            lb4['text'] = 'Obesidade Grau 2!'
            lb4['fg'] = 'orange'
        elif 40 <= lb3['text']:
            lb4['text'] = 'Obesidade Grau 3!'
            lb4['fg'] = 'red'
        else:
            pass
    else:
        lb3['text'] = 'Entrada Invalida!'


def clear():
    en1.delete(0, END)
    en2.delete(0, END)
    lb3['text'] = 'Resultado'
    lb4['text'] = ''


root = Tk()
# o botão enter do teclado chama a função imc
root.bind('<Return>', lambda event: imc())
root.bind('<F5>', lambda event: clear())


en1 = Entry(root, font='Arial 26')
en2 = Entry(root, font='Arial 26')
bt1 = Button(root, text='IMC', font='Arial 26', command=imc)
bt2 = Button(root, text='Limpar', font='Arial 26', command=clear)
lb1 = Label(root, text='Peso', font='Arial 26')
lb2 = Label(root, text='Altura', font='Arial 26')
lb3 = Label(root, text='Resultado', font='Arial 26')
lb4 = Label(root, text='', font='Arial 26')


lb1.grid(row=0, column=0)
en1.grid(row=0, column=1)
lb2.grid(row=1, column=0)
en2.grid(row=1, column=1)
bt1.grid(row=2, column=1)
lb3.grid(row=3, column=1)
lb4.grid(row=4, column=1)
bt2.grid(row=5, column=1)

root.mainloop()