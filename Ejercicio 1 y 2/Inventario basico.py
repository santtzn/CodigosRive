inventario = {}
print("Inventario basico")
opcion = 0
while opcion != 4:
    print("1. Agregar producto")
    print("2. Vender producto")
    print("3. Mostrar inventario")
    opcion = int(input("Elige una opcion: "))
    if opcion == 1:
        nombre = input("Producto: ")
        cantidad = int(input("Cantidad: "))
        inventario[nombre] = inventario.get(nombre, 0)+ cantidad
        print("Producto agregado")
    elif opcion == 2:
        nombre = input("Producto vendido: ")
        cantidad = int(input("Cantidad vendida: "))
        if nombre in inventario and inventario[nombre] >= cantidad:
            inventario[nombre] = inventario[nombre] -  cantidad
        else:
            print("No hay suficiente producto")
    elif opcion == 3:
        for producto, cantidad in inventario.items():
            print(producto, cantidad)
print("Programa terminado")
