
from tkinter import *


def decrementar():
    valor = int (lbl_valor["text"])
    lbl_valor["text"] = f"{valor - 1}"
    

ventana = Tk()
ventana.geometry("300x100")
ventana.title("ContDecreciente")
ventana.rowconfigure(0, minsize=50, weight=1)
ventana.columnconfigure([0,1,2], minsize=50, weight=1)


boton = Button (ventana, text="-", command= decrementar)
boton.grid(row=0, column=2, sticky="nsew")

lbl_contador = Label (ventana, text="Contador")
lbl_contador.grid(row=0, column=0)
lbl_valor = Label(ventana, text= "88")
lbl_valor.grid(row=0, column=1)


ventana.mainloop()


