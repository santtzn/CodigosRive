def pedir_calificacion(numero):
    calificacion = float(input("Ingresa la calificacion: "))
    while calificacion < 0 or calificacion > 10:
        print("Calificacion invalida")
        calificacion = float(input("Captura de nuevo: "))
    return calificacion
print("Registo de calificaciones")
cantidad = int(input("Cuantos alumnos van a registar?: "))
alumnos = []
for i in range(cantidad):
    nombre = input("Nombre del alumno: ")
    c1 = pedir_calificacion(1)
    c2 = pedir_calificacion(2)
    c3 = pedir_calificacion(3)
    promedio = (c1+c2+c3)/3
    if promedio >= 6:
        estado = "Aprobado"
    else:
        estado = "Reprobado"
    alumnos.append({
        "nombre": nombre,
        "promedio": promedio,
        "estado": estado
    })
    print("Alumno registrado")
print("Resultados")
for alumno in alumnos:
    print(alumno["nombre"], alumno["promedio"], alumno["estado"])
