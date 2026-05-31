#Calculadora funcional
from tkinter import *
def sumar():
    resultado = float(entrada1.get()) + float(entrada2.get())
    etiqueta_resultado.config(text="Resultado: " + str(resultado))
def restar():
    resultado = float(entrada1.get()) - float(entrada2.get())
    etiqueta_resultado.config(text="Resultado: " + str(resultado))
def multiplicar():
    resultado = float(entrada1.get()) * float(entrada2.get())
    etiqueta_resultado.config(text="Resultado: " + str(resultado))
def dividir():
    num1 = float(entrada1.get())
    num2 = float(entrada2.get())
    if num2 == 0:
        etiqueta_resultado.config(text="Error: división entre cero")
    else:
        resultado = num1 / num2
        etiqueta_resultado.config(text="Resultado: " + str(resultado))
ventana = Tk()
ventana.title("Calculadora funcional")
ventana.geometry("400x300")
Label(ventana, text="Primer número").pack()
entrada1 = Entry(ventana)
entrada1.pack()
Label(ventana, text="Segundo número").pack()
entrada2 = Entry(ventana)
entrada2.pack()
Button(ventana, text="Sumar", command=sumar).pack()
Button(ventana, text="Restar", command=restar).pack()
Button(ventana, text="Multiplicar", command=multiplicar).pack()
Button(ventana, text="Dividir", command=dividir).pack()
etiqueta_resultado = Label(ventana, text="Resultado:")
etiqueta_resultado.pack()
ventana.mainloop()
