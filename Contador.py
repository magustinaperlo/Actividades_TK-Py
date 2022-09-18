
from tkinter import *


def incrementar():
    valor = int (lbl_valor["text"])
    lbl_valor["text"] = f"{valor + 1}"


def decrementar():
    valor = int (lbl_valor["text"])
    lbl_valor["text"] = f"{valor - 1}"


def reset ():
    valor = int (lbl_valor["text"])
    lbl_valor["text"] = 0




ventana = Tk()
ventana.geometry("300x100")
ventana.title("Contador")


frameCont = Frame(ventana)
frameCont.place(relx= 0.5, rely=0.5, anchor=CENTER)

boton_inc = Button (frameCont, text="CountUp", command= incrementar)
boton_inc.grid(row=0, column=2, sticky="nsew")

boton_dec = Button (frameCont, text="CountDown", command= decrementar)
boton_dec.grid(row=0, column=3, sticky="nsew")

boton_reset = Button(frameCont, text="Reset", command= reset )
boton_reset.grid(row=0, column=4, sticky="nsew")

lbl_contador = Label (frameCont, text="Contador")
lbl_contador.grid(row=0, column=0, sticky="nsew")

lbl_valor = Label(frameCont, text= "0")
lbl_valor.grid(row=0, column=1, sticky="nsew")



ventana.mainloop()


