from tkinter import *

def suma():
    a = int(num1.get())
    b = int(num2.get())
    c = a + b
    numResultado.set(c)

def resta():
    a = int(num1.get())
    b = int(num2.get())
    c = a-b
    numResultado.set(c)

def producto():
    a = int(num1.get())
    b = int(num2.get())
    c = a*b
    numResultado.set(c)

def division():
    a = int(num1.get())
    b = int(num2.get())
    c = a/b
    numResultado.set(c)

def mod():
    a = int(num1.get())
    b = int(num2.get())
    c = a%b
    numResultado.set(c)

def clear():
    num1.set("")
    num2.set("")
    numResultado.set("")


ventana = Tk()
ventana.geometry("300x200")
ventana.title("Calculadora")
ventana.configure(background="SkyBlue4")

frameCalc = Frame(ventana)
frameCalc.place(relx= 0.5, rely=0.5, anchor=CENTER)


num1= StringVar()
num2= StringVar()
numResultado= StringVar()
num1.set("")
num2.set("")
numResultado.set("")


num1text=Label(frameCalc, text="Primer numero")
num1text.grid(row=0, column=0)

num2text=Label(frameCalc, text="Segundo numero")
num2text.grid(row=1, column=0)

resultadotext=Label(frameCalc, text="Resultado")
resultadotext.grid(row=2, column=0)


num1 = Entry(frameCalc, textvariable=num1)
num1.grid(row=0, column=1)

num2 = Entry(frameCalc, textvariable=num2)
num2.grid(row=1, column=1)

resultado = Entry(frameCalc, state="readonly", textvariable=numResultado)
resultado.grid(row=2, column=1)


suma = Button(frameCalc, text="     +     ", command=suma)
suma.grid(row=4, column=0)

resta = Button(frameCalc, text="     -     ", command=resta)
resta.grid(row=4, column=1)

producto = Button(frameCalc, text="      *     ", command=producto)
producto.grid(row=5, column=0)

division = Button(frameCalc, text="      /    ", command=division)
division.grid(row=5, column=1)

mod = Button(frameCalc, text="     %    ", command=mod)
mod.grid(row=6, column=0)

clear = Button(frameCalc, text="CLEAR", command=clear)
clear.grid(row=6, column=1)




ventana.mainloop()

