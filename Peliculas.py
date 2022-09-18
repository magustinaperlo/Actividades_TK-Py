from tkinter import *



def Añadir():
    peli = peliculas.get() 
    lista.insert(END, peli) 
    peliculas.delete(0, END) 


ventana = Tk()
ventana.geometry("300x250")
ventana.title("Peliculas")

peliculas = StringVar()
peliculas.set("")

framePeli = Frame(ventana)
framePeli.pack()

lbl_pelicula = Label(framePeli, text="Escribe el titulo de una pelicula")
lbl_pelicula.grid(row=0, column=0)

lbl_list_pelicula = Label(framePeli, text="Peliculas")
lbl_list_pelicula.grid(row=0, column=1)

peliculas = Entry(framePeli, textvariable=peliculas)
peliculas.grid(row=1, column=0)

lista = Listbox(framePeli)
lista.grid(row=1, column=1)

boton_Pelicula = Button(framePeli, text="Añadir", command=Añadir)
boton_Pelicula.grid(row=2, column=0)



ventana.mainloop()