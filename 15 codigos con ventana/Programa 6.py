from tkinter import *
def restar():
    num1 = int(entrada1.get())
    num2 = int(entrada2.get())
    resultado = num1 - num2
    texto_resultado.config(text="Resultado: " + str(resultado))
ventana = Tk()
ventana.title("Programa 6")
Label(ventana, text="Minuendo").pack()
entrada1 = Entry(ventana)
entrada1.pack()
Label(ventana, text="Sustraendo").pack()
entrada2 = Entry(ventana)
entrada2.pack()
Button(ventana, text="Restar", command=restar).pack()
texto_resultado = Label(ventana, text="")
texto_resultado.pack()
ventana.mainloop()
