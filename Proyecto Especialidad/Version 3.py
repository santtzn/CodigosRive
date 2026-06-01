from tkinter import *
def analizar():
    lugar = entrada_lugar.get()
    problema = entrada_problema.get()
    if lugar == "escuela" and problema == "bullying":
        etiqueta_resultado.config(text = "Busca ayuda de un maestro.")
    elif lugar == "casa" and problema == "miedo":
        etiqueta_resultado.config(text = "Busca ayuda de un adulto.")
    elif lugar == "internet":
        etiqueta_resultado.config(text = "Posible acoso digital.")
    else:
        etiqueta_resultado.config(text = "No identificado.")
ventana = Tk()
ventana.title("Version 3")
ventana.geometry("450x250")
Label(ventana, text = "Lugar").pack()
entrada_lugar = Entry(ventana)
entrada_lugar.pack()
Label(ventana, text = "Problema").pack()
entrada_problema = Entry(ventana)
entrada_problema.pack()
Button(ventana, text = "Analizar", command = analizar).pack()
etiqueta_resultado = Label(ventana, text = "")
etiqueta_resultado.pack()
ventana.mainloop()
