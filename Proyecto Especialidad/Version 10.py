from tkinter import *
from tkinter import messagebox
puertas_superadas = 0
nombre_jugador = ""
def iniciar_aventura():
    global nombre_jugador
    nombre_jugador = entrada_nombre.get()
    if nombre_jugador == "":
        messagebox.showinfo(
            "Aviso",
            "Escribe tu nombre.")
        return
    ventana_historia = Toplevel()
    ventana_historia.title("Alex")
    ventana_historia.geometry("600x400")
    Label(
        ventana_historia,
        text = "¡Hola " + nombre_jugador + "!",
        font = ("Arial",16,"bold")).pack(pady = 10)

    Label(
        ventana_historia, text =
        "Soy Alex.\n\n"
        "He quedado atrapado en la Escuela del Cambio.\n"
        "Necesito tu ayuda para salir.\n\n"
        "Debemos atravesar 5 puertas.\n"
        "Cada una representa un problema social.",
        font = ("Arial",12)).pack(pady = 20)
    Button(
        ventana_historia,
        text = "Comenzar Aventura",
        command = lambda:[
            ventana_historia.destroy(),
            puerta1()]).pack(pady = 20)
def puerta1():
    ventana = Toplevel()
    ventana.title("Puerta 1")
    ventana.geometry("600x400")
    Label(
        ventana,
        text = "PUERTA 1",
        font = ("Arial",18,"bold")).pack(pady = 10)
    Label(
        ventana, text =
        "Un estudiante está siendo excluido\n"
        "durante el recreo.\n\n"
        "¿Qué harías?",
        font = ("Arial",12)).pack()
    respuesta = Entry(ventana)
    respuesta.pack(pady = 10)
    def revisar():
        global puertas_superadas
        texto = respuesta.get().lower()
        if "ayud" in texto or "apoy" in texto or "inclu" in texto:
            puertas_superadas += 1
            messagebox.showinfo(
                "Correcto",
                "¡Excelente!\nLa puerta se abre.")
            ventana.destroy()
            puerta2()
        else:
            messagebox.showinfo(
                "Pista",
                "Intenta pensar en una acción solidaria.")
    Button(
        ventana,
        text = "Abrir Puerta",
        command = revisar).pack(pady = 20)
def puerta2():
    ventana = Toplevel()
    ventana.title("Puerta 2")
    ventana.geometry("600x400")
    Label(
        ventana,
        text = "PUERTA 2",
        font = ("Arial",18,"bold")).pack(pady = 10)
    Label(
        ventana, text =
        "Un compañero recibe mensajes\n"
        "ofensivos en internet.\n\n"
        "¿Qué le recomendarías?",
        font = ("Arial",12)).pack()
    respuesta = Entry(ventana)
    respuesta.pack(pady = 10)
    def revisar():
        global puertas_superadas
        texto = respuesta.get().lower()
        if "report" in texto or "bloque" in texto or "ayud" in texto:
            puertas_superadas += 1
            messagebox.showinfo(
                "Correcto",
                "¡Bien hecho!")
            ventana.destroy()
            puerta3()
        else:
            messagebox.showinfo(
                "Pista",
                "Piensa en una acción segura.")
    Button(
        ventana,
        text = "Abrir Puerta",
        command = revisar).pack(pady = 20)
def puerta3():
    ventana = Toplevel()
    ventana.title("Puerta 3")
    ventana.geometry("600x400")
    Label(
        ventana,
        text = "PUERTA 3",
        font = ("Arial",18,"bold")).pack(pady = 10)
    Label(
        ventana, text =
        "Un amigo está muy triste.\n\n"
        "¿Qué harías por él?",
        font = ("Arial",12)).pack()
    respuesta = Entry(ventana)
    respuesta.pack(pady = 10)
    def revisar():
        global puertas_superadas
        texto = respuesta.get().lower()
        if "escuch" in texto or "apoy" in texto or "hablar" in texto:
            puertas_superadas += 1
            messagebox.showinfo(
                "Correcto",
                "La puerta se abre.")
            ventana.destroy()
            puerta4()
        else:
            messagebox.showinfo(
                "Pista",
                "Piensa en cómo acompañarías a alguien.")
    Button(
        ventana,
        text = "Abrir Puerta",
        command = revisar).pack(pady = 20)
def puerta4():
    ventana = Toplevel()
    ventana.title("Puerta 4")
    ventana.geometry("600x400")
    Label(
        ventana,
        text = "PUERTA 4",
        font = ("Arial",18,"bold")).pack(pady = 10) 
    Label(
        ventana,
        text =
        "Observas un acto de discriminación.\n\n"
        "¿Qué harías?",
        font = ("Arial",12)).pack()
    respuesta = Entry(ventana)
    respuesta.pack(pady = 10)
    def revisar():
        global puertas_superadas
        texto = respuesta.get().lower()
        if "report" in texto or "ayud" in texto or "defend" in texto:
            puertas_superadas += 1
            messagebox.showinfo(
                "Correcto",
                "¡Muy bien!")
            ventana.destroy()
            puerta5()
        else:
            messagebox.showinfo(
                "Pista",
                "Piensa en actuar con respeto.")
    Button(
        ventana,
        text = "Abrir Puerta",
        command = revisar).pack(pady = 20)
def puerta5():
    ventana = Toplevel()
    ventana.title("Puerta 5")
    ventana.geometry("600x400")
    Label(
        ventana,
        text = "PUERTA 5",
        font = ("Arial",18,"bold")).pack(pady = 10)
    Label(
        ventana, text =
        "Un estudiante tiene miedo\n"
        "de participar en clase.\n\n"
        "¿Cómo podrías ayudarlo?",
        font = ("Arial",12)).pack()
    respuesta = Entry(ventana)
    respuesta.pack(pady=10)
    def revisar():
        global puertas_superadas
        texto = respuesta.get().lower()
        if "anim" in texto or "apoy" in texto or "ayud" in texto:
            puertas_superadas += 1
            ventana.destroy()
            final_juego()
        else:
            messagebox.showinfo(
                "Pista",
                "Piensa en cómo darle confianza.")
    Button(
        ventana,
        text = "Abrir Puerta",
        command = revisar).pack(pady = 20)
def final_juego():
    ventana_final = Toplevel()
    ventana_final.title("Final")
    ventana_final.geometry("600x400")
    Label(
        ventana_final,
        text = "¡FELICIDADES!",
        font = ("Arial",20,"bold")).pack(pady = 20)
    Label(
        ventana_final, text =
        "Has ayudado a Alex a escapar.\n\n"
        "Puertas superadas: " +
        str(puertas_superadas) +
        "/5",
        font = ("Arial",14)).pack(pady = 20)
    Label(
        ventana_final, text =
        "Valores demostrados:\n\n"
        "✓ Empatía\n"
        "✓ Inclusión\n"
        "✓ Respeto\n"
        "✓ Solidaridad\n"
        "✓ Responsabilidad",
        font = ("Arial",12)).pack()
ventana_principal = Tk()
ventana_principal.title("Escapando de la Escuela del Cambio")
ventana_principal.geometry("700x500")
Label(
    ventana_principal,
    text = "ESCAPANDO DE LA ESCUELA DEL CAMBIO",
    font = ("Arial",20,"bold")).pack(pady = 20)
Label(
    ventana_principal,
    text = "Ingresa tu nombre para comenzar",
    font = ("Arial",12)).pack()
entrada_nombre = Entry(
    ventana_principal)
entrada_nombre.pack(pady = 10)
Button(
    ventana_principal,
    text = "Comenzar",
    command = iniciar_aventura).pack(pady = 20)
ventana_principal.mainloop()
