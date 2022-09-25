from tkinter import *
from random import *
from tkinter import messagebox


ventana = Tk()
ventana.geometry("300x150")
ventana.title("Generador de numeros")

def Random():
    a = int(caja_Num1.get())
    b = int(caja_Num2.get())
    if a > b:
        # msg="ERROR"
        # numResultado.set(msg)
        #otra opcion es orientar al usuario sobre el error para que pueda ejecutar bien el programa
        messagebox.showinfo(message="Número 1 debe ser menor a número 2", title="Error")
    else:
        c = randint(a,b)
        numResultado.set(c)

numResultado = StringVar()
numResultado.set("")

frame = Frame(ventana)
frame.pack()

lbl_Num1 = Label(frame, text="Número 1")
lbl_Num1.grid(row=0,column=0) 
lbl_Num2 = Label(frame, text="Número 2")
lbl_Num2.grid(row=1,column=0)
lbl_NumGen = Label(frame, text="Número Generado")
lbl_NumGen.grid(row=2,column=0)

#se añade el state=readonly para que el usuario solo manipule los números desde el widget
caja_Num1 = Spinbox(frame, from_= 0 ,to=999,state="readonly")  
caja_Num1.grid(row=0,column=1)
caja_Num2 = Spinbox(frame, from_= 0 ,to= 999,state="readonly") 
caja_Num2.grid(row=1,column=1)
entrada_Resultado = Entry(frame, state="readonly", textvariable=numResultado) 
entrada_Resultado.grid(row=2,column=1)


boton_Generar = Button(frame, text="Generar", command=Random)
boton_Generar.grid(row=3, column=1)

ventana.mainloop()
