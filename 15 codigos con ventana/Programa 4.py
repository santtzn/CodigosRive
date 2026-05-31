from  tkinter import *
def sumar():
    num1 = int(entrada1.get())
    num2 = int(entrada2.get())
    resultado = num1 + num2
    texto_resultado.config(text="Resultado: " + str(resultado))
ventana = Tk()
ventana.title("Programa 4")
Label(ventana, text="Primer numero").pack()
entrada1 = Entry(ventana)
entrada1.pack()
Label(ventana, text="Segundo numero").pack()
entrada2 = Entry(ventana)
entrada2.pack()
Button(ventana, text="Sumar", command=sumar).pack()
texto_resultado = Label(ventana, text="")
texto_resultado.pack()
ventana.mainloop()
