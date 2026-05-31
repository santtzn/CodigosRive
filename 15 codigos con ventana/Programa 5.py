from tkinter import *
def sumar():
    num1 = float(entrada1.get())
    num2 = float(entrada2.get())
    resultado = num1 + num2
    texto_resultado.config(text="Resultado: " + str(resultado))
ventana = Tk()
ventana.title("Programa 5")
Label(ventana, text="Primer decimal").pack()
entrada1 = Entry(ventana)
entrada1.pack()
Label(ventana, text="Segundo decimal").pack()
entrada2 = Entry(ventana)
entrada2.pack()
Button(ventana, text="Sumar", command=sumar).pack()
texto_resultado = Label(ventana, text="")
texto_resultado.pack()
ventana.mainloop()
