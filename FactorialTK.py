from tkinter import *


def factorial():
    numN=1+int(entrada.get())
    numF=1
    for i in range (1, numN+1):
        numF = numF * i
    txt1.set(numN)
    txt2.set(numF)

ventana = Tk()
ventana.geometry("400x100")
ventana.title("Factorial")

txt1 =  StringVar()
txt2 =  StringVar()
txt1.set(1)
txt2.set(1)


frameFact = Frame(ventana)
frameFact.place(relx= 0.5, rely=0.5, anchor=CENTER)

lbl_1 = Label(frameFact, text="n")
lbl_1.grid(row=0, column=0)

entrada = Entry(frameFact,state="readonly", textvariable=txt1)
entrada.grid(row=0, column=1)

lbl_2 = Label(frameFact, text="Factorial(n)")
lbl_2.grid(row=0, column=2)

entada2 = Entry(frameFact, state="readonly", textvariable=txt2)
entada2.grid(row=0, column=3)

boton= Button(frameFact, text="Siguiente", command=factorial)
boton.grid(row=0, column=4)


ventana.mainloop()