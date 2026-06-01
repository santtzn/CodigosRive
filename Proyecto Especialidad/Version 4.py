from tkinter import *
def analizar():
    nombre = entrada_nombre.get()
    lugar = entrada_lugar.get()
    problema = entrada_problema.get()
    if lugar == "escuela" and problema == "bullying":
        etiqueta_resultado.config(text = "Hola " + nombre + "\nPosible bullying escolar, habla con un maestro.")
    else:
        etiqueta_resultado.config(text = "Hola " + nombre +

            "\nLo siento. Tu problema no fue identificado.")
ventana = Tk()
ventana.title("Version 4")
ventana.geometry("450x300")
Label(ventana, text = "Nombre").pack()
entrada_nombre = Entry(ventana)
entrada_nombre.pack()
Label(ventana,text = "Lugar").pack()
entrada_lugar = Entry(ventana)
entrada_lugar.pack()
Label(ventana, text = "Problema").pack()
entrada_problema = Entry(ventana)
entrada_problema.pack()
Button(ventana, text = "Analizar", command = analizar).pack()
etiqueta_resultado = Label(ventana, text = "")
etiqueta_resultado.pack()
ventana.mainloop()
