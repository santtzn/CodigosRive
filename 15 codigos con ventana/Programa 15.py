from tkinter import *
ventana = Tk()
ventana.title("Programa 15")
ventana.geometry("200x100")
lista = ["ordenador", "teclado", "raton"]
Label(ventana, text=lista).pack()
ventana.mainloop()
