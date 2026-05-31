from tkinter import *
def multiplicar():
    num1 = int(entrada1.get())
    num2 = int(entrada2.get())
    resultado = num1 * num2
    texto_resultado.config(text="Resultado: " + str(resultado))
ventana = Tk()
ventana.title("Programa 8")
Label(ventana, text="Multiplicando").pack()
entrada1 = Entry(ventana)
entrada1.pack()
Label(ventana, text="multiplicador").pack()
entrada2 = Entry(ventana)
entrada2.pack()
Button(ventana, text="Multiplicar", command=multiplicar).pack()
texto_resultado = Label(ventana, text="")
texto_resultado.pack()
ventana.mainloop()
