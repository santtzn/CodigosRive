from tkinter import *
def analizar():
    problema = entrada_problema.get()
    if problema == "bullying":
        etiqueta_resultado.config(text = "Habla con un maestro.")
ventana = Tk()
ventana.title("Version 1")
ventana.geometry("400x200")
etiqueta_problema = Label(ventana, text = "Escribe tu problema")
etiqueta_problema.pack()
entrada_problema = Entry(ventana)
entrada_problema.pack()
boton = Button(ventana, text = "Analizar", command = analizar)
boton.pack()
etiqueta_resultado = Label(ventana, text = "")
etiqueta_resultado.pack()
ventana.mainloop()
