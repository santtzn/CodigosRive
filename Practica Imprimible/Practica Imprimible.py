from tkinter import *
class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
    def vender(self, cantidad_vendida):
        if cantidad_vendida > self.cantidad:
            return "No hay existencia"
        total = self.precio * cantidad_vendida
        if cantidad_vendida >= 5:
            total = total * 0.9
        self.cantidad = self.cantidad - cantidad_vendida
        return total
    def reabastecer(self, cantidad_agregada):
        self.cantidad = self.cantidad + cantidad_agregada
    def mostrar_info(self):
        return self.nombre
def calcular():
    p = Producto(
        entrada_nombre.get(),
        float(entrada_precio.get()),
        int(entrada_cantidad.get())
    )
    resultado_venta = p.vender(
        int(entrada_vender.get())
    )
    resultado.config(text=str(resultado_venta))
ventana = Tk()
ventana.title("Cafeteria")
ventana.geometry("350x300")
Label(ventana, text = "Nombre").pack()
entrada_nombre = Entry(ventana)
entrada_nombre.pack()
Label(ventana, text = "Precio").pack()
entrada_precio = Entry(ventana)
entrada_precio.pack()
Label(ventana, text = "Cantidad disponible").pack()
entrada_cantidad = Entry(ventana)
entrada_cantidad.pack()
Label(ventana, text = "Cantidad a vender").pack()
entrada_vender = Entry(ventana)
entrada_vender.pack()
resultado = Label(ventana, text="")
resultado.pack()
Button(ventana, text = "Calcular Venta", command=calcular).pack()
ventana.mainloop()
