from tkinter import *
def abrir_sistema():
    ventana_sistema = Toplevel()
    ventana_sistema.title("Sistema de Apoyo Social")
    ventana_sistema.geometry("600x500")
    def analizar():
        nombre = entrada_nombre.get()
        edad = entrada_edad.get()
        lugar = entrada_lugar.get()
        problema = entrada_problema.get()
        if nombre == "":
            etiqueta_resultado.config(text = "Escribe tu nombre.")
        elif edad == "":
            etiqueta_resultado.config(text = "Escribe tu edad.")
        elif lugar == "":
            etiqueta_resultado.config(text = "Escribe el lugar.")
        elif problema == "":
            etiqueta_resultado.config(text = "Escribe el problema.")
        elif lugar == "escuela" and problema == "bullying":
            etiqueta_resultado.config(
                text = "Hola " + nombre +
                "\nEdad: " + edad +
                "\n\nPosible caso de bullying." +
                "\n\nRecomendaciones:" +
                "\n- Habla con un maestro." +
                "\n- Habla con tus padres." +
                "\n- No respondas con violencia.")
        elif lugar == "internet" and problema == "acoso":
            etiqueta_resultado.config(
                text = "Hola " + nombre +
                "\nEdad: " + edad +
                "\n\nPosible acoso digital." +
                "\n\nRecomendaciones:" +
                "\n- Bloquea al usuario." +
                "\n- Reporta la cuenta.")
        elif problema == "tristeza":
            etiqueta_resultado.config(
                text = "Hola " + nombre +
                "\nEdad: " + edad +
                "\n\nHabla con alguien de confianza.")
        elif problema == "amenazas":
            etiqueta_resultado.config(
                text = "Hola " + nombre +
                "\nEdad: " + edad +
                "\n\nBusca ayuda de un adulto.")
        else:
            etiqueta_resultado.config(text = "Problema no identificado.")
    def informacion():
        etiqueta_resultado.config(
            text = "Problemas reconocidos:\n\n"
                 "bullying\n"
                 "acoso\n"
                 "tristeza\n"
                 "amenazas")
    etiqueta_titulo = Label(ventana_sistema, text = "SISTEMA DE APOYO SOCIAL")
    etiqueta_titulo.pack()
    etiqueta_nombre = Label(ventana_sistema, text = "Nombre")
    etiqueta_nombre.pack()
    entrada_nombre = Entry(ventana_sistema)
    entrada_nombre.pack()
    etiqueta_edad = Label(ventana_sistema, text = "Edad")
    etiqueta_edad.pack()
    entrada_edad = Entry(ventana_sistema)
    entrada_edad.pack()
    etiqueta_lugar = Label(ventana_sistema, text = "Lugar")
    etiqueta_lugar.pack()
    entrada_lugar = Entry(ventana_sistema)
    entrada_lugar.pack()
    etiqueta_problema = Label(ventana_sistema, text = "Problema")
    etiqueta_problema.pack()
    entrada_problema = Entry(ventana_sistema)
    entrada_problema.pack()
    boton_analizar = Button(ventana_sistema, text = "Analizar", command = analizar)
    boton_analizar.pack()
    boton_informacion = Button(ventana_sistema, text = "Problemas que reconoce el sistema", command = informacion)
    boton_informacion.pack()
    etiqueta_resultado = Label(ventana_sistema, text = "")
    etiqueta_resultado.pack()
ventana = Tk()
ventana.title("Bienvenida")
ventana.geometry("400x300")
etiqueta_bienvenida = Label(ventana, text = "BIENVENIDO AL SISTEMA DE APOYO SOCIAL")
etiqueta_bienvenida.pack()
etiqueta_texto = Label(ventana, text="Este programa ayuda a identificar\nproblemas sociales y dar recomendaciones.")
etiqueta_texto.pack()
boton_entrar = Button(ventana, text = "Entrar al Sistema", command = abrir_sistema)
boton_entrar.pack()
ventana.mainloop()
