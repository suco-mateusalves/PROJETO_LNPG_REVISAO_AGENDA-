from tkinter import *

def limparDados():
    nomeEntry.delete("0", END)
    telefoneEntry.delete("0", END)
    emailEntry.delete("0", END)


def gravarDados():
    nome1 = nomeEntry.get()
    telefone1= telefoneEntry.get()
    email1 = emailEntry.get()
    preferencial1 = prefe00.get()
    with open("contatos.txt","a",encoding="utf-8") as file:
        file.write(f"{nome1},{telefone1},{email1},{preferencial1}\n")
        file.close()

def leitura():
    with open("contatos.txt","r",encoding="utf-8") as file:
        
        file2 = file.readlines()
        print(file2)
        lista = []

        for x in file2:
            lista.append(x.split(","))

        print(lista)

        mostraCaixaDeTexto(lista)

        file.close()
def mostraCaixaDeTexto(dados):
    textMostrar.insert()


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

buttonEnviar = Button(root,text="Gravar", command=gravarDados)
buttonEnviar.place(x=130,y=140)

buttonLimpar = Button(root,text="Limpar", command=limparDados)
buttonLimpar.place(x=130,y=160)

botaoler = Button(root,text="ler", command=leitura)
botaoler.place(x=170,y=160)

textMostrar = Text(root, x=200, y=300)
textMostrar.place(x= 100, y=200)

root.mainloop()