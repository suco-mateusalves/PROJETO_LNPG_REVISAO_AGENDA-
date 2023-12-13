from tkinter import *
def gravarDados():
    with open("contatos.txt","a",encoding="utf-8") as file:
        file.write()


#Cria janela
root = Tk()
root.title("Agenda de Contatos")
root.geometry("850x850")

nome = Label(root, text="Nome:")
nome.place(x=50, y=50)

telefone = Label(root, text="Telefone:")
telefone.place(x=50, y=70)

email = Label(root, text="E-mail:")
email.place(x=50, y=90)

preferencial = Label(root, text="Preferencial:")
preferencial.place(x=50, y=110)

nomeEntry = Entry(root)
nomeEntry.place(x=130, y=50)

telefoneEntry = Entry(root)
telefoneEntry.place(x=130, y=70)

emailEntry = Entry(root)
emailEntry.place(x=130, y=90)

prefe00 = StringVar()
prefe00.set("sim")
prefe00radiobuton1 = Radiobutton(root,text="Sim", variable=prefe00, value="sim")
prefe00radiobuton1.place(x=130,y=110)
prefe00radiobuton2 = Radiobutton(root,text="Não", variable=prefe00, value="não")
prefe00radiobuton2.place(x=200,y=110)

buttonEnviar = Button(root,text="Gravar")
buttonEnviar.place(x=130,y=140)


root.mainloop()