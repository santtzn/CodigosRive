from tkinter import *
def dividir():
    num1 = float(entrada1.get())
    num2 = float(entrada2.get())
    resultado = num1 / num2
    texto_resultado.config(text="Resultado: " + str(resultado))
ventana = Tk()
ventana.title("Programa 11")
Label(ventana, text="Primer decimal").pack()
entrada1 = Entry(ventana)
entrada1.pack()
Label(ventana, text="Segundo decimal").pack()
entrada2 = Entry(ventana)
entrada2.pack()
Button(ventana, text="Dividir", command=dividir).pack()
texto_resultado = Label(ventana, text="")
texto_resultado.pack()
ventana.mainloop()
