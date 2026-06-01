from tkinter import *
def analizar():
    problema = entrada_problema.get()
    if problema == "bullying":
        etiqueta_resultado.config(text = "Habla con un maestro.")
    elif problema == "tristeza":
        etiqueta_resultado.config(text = "Habla con alguien de confianza.")
    elif problema == "miedo":
        etiqueta_resultado.config(text = "Busca apoyo de un adulto.")
    else:
        etiqueta_resultado.config(text = "Problema no identificado.")
ventana = Tk()
ventana.title("Version 2")
ventana.geometry("400x250")
etiqueta_problema = Label(ventana, text = "Escribe tu problema")
etiqueta_problema.pack()
entrada_problema = Entry(ventana)
entrada_problema.pack()
boton = Button(ventana, text = "Analizar", command = analizar)
boton.pack()
etiqueta_resultado = Label(ventana, text = "")
etiqueta_resultado.pack()
ventana.mainloop()
