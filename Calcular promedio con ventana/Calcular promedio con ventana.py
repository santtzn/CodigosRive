from tkinter import *
def calcular_promedio(c1, c2, c3):
    promedio = (c1+c2+c3)/3
    return promedio
def mostrar_resultado():
    c1 = float(entry1.get())
    c2 = float(entry2.get())
    c3 = float(entry3.get())
    promedio = calcular_promedio(c1, c2, c3)
    resultado.config(text = "Promedio: " + str(round(promedio, 2)))
ventana = Tk()
ventana.title("Promedio del Alumno")
ventana.geometry("350x250")
Label(ventana, text = "Calificacion 1").pack()
entry1 = Entry(ventana)
entry1.pack()
Label(ventana, text = "Calificacion 2").pack()
entry2 = Entry(ventana)
entry2.pack()
Label(ventana, text = "Calificacion 3").pack()
entry3 = Entry(ventana)
entry3.pack()
Button(ventana, text = "Calcular Promedio", command = mostrar_resultado).pack()
resultado = Label(ventana, text = "Promedio: ")
resultado.pack()
ventana.mainloop()
