from tkinter import *
ventana = Tk()
ventana.title("Programa 14")
ventana.geometry("350x200")
cadena = "Hola Time of Software\nEsto es una cadena\nmultilinea"
Label(ventana, text=cadena).pack()
ventana.mainloop()
