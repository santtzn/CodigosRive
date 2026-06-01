from tkinter import *
def analizar():
    nombre = entrada_nombre.get()
    lugar = entrada_lugar.get()
    problema = entrada_problema.get()
    if lugar == "escuela" and problema == "bullying":
        etiqueta_resultado.config(text = "Hola " + nombre + "\n\nPosible bullying." + "\n\nRecomendaciones:" + "\nHabla con un maestro." + "\nHabla con tus padres." + "\nNo respondas con violencia.")
    elif lugar == "internet":
        etiqueta_resultado.config(text = "Hola " + nombre + "\n\nPosible acoso digital." + "\n\nRecomendaciones:" + "\nBloquea al usuario." + "\nReporta la cuenta.")
    elif problema == "tristeza":
        etiqueta_resultado.config(text = "Hola " + nombre + "\n\nHabla con alguien de confianza.")
    else:
        etiqueta_resultado.config(text = "Problema no identificado.")
ventana = Tk()
ventana.title("Version 5")
ventana.geometry("500x350")
Label(ventana, text = "Nombre").pack()
entrada_nombre = Entry(ventana)
entrada_nombre.pack()
Label(ventana, text = "Lugar").pack()
entrada_lugar = Entry(ventana)
entrada_lugar.pack()
Label(ventana, text = "Problema").pack()
entrada_problema = Entry(ventana)
entrada_problema.pack()
Button(ventana, text = "Analizar", command=analizar).pack()
etiqueta_resultado = Label(ventana, text="")
etiqueta_resultado.pack()
ventana.mainloop()
