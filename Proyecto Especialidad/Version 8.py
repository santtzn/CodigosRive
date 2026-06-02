from tkinter import *
def abrir_sistema():
    ventana_sistema = Toplevel()
    ventana_sistema.title("Sistema de Apoyo Social")
    ventana_sistema.geometry("700x600")
    ventana_sistema.configure(bg="lightyellow")
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
        else:
            texto_lugar = ""
            if lugar == "escuela":
                texto_lugar = "\n\nEl problema ocurre en la escuela."
            elif lugar == "casa":
                texto_lugar = "\n\nEl problema ocurre en casa."
            elif lugar == "internet":
                texto_lugar = "\n\nEl problema ocurre en internet."
            elif lugar == "comunidad":
                texto_lugar = "\n\nEl problema ocurre en la comunidad."
            if problema == "bullying":
                etiqueta_resultado.config(
                    text = "Hola " + nombre +
                    "\nEdad: " + edad +
                    "\n\nPosible caso de bullying." +
                    "\n\nRecomendaciones:" +
                    "\n- Habla con un maestro." +
                    "\n- Habla con tus padres." +
                    "\n- No respondas con violencia." +
                    texto_lugar)
            elif problema == "miedo":
                etiqueta_resultado.config(
                    text = "Hola " + nombre +
                    "\nEdad: " + edad +
                    "\n\nSituación de miedo." +
                    "\n\nRecomendaciones:" +
                    "\n- Habla con un adulto de confianza." +
                    "\n- Expresa lo que sientes." +
                    texto_lugar)
            elif problema == "tristeza":
                etiqueta_resultado.config(
                    text = "Hola " + nombre +
                    "\nEdad: " + edad +
                    "\n\nPosible problema emocional." +
                    "\n\nRecomendaciones:" +
                    "\n- Habla con alguien de confianza." +
                    "\n- Realiza actividades que disfrutes." +
                    texto_lugar)
            elif problema == "acoso":
                etiqueta_resultado.config(
                    text = "Hola " + nombre +
                    "\nEdad: " + edad +
                    "\n\nPosible acoso." +
                    "\n\nRecomendaciones:" +
                    "\n- Busca apoyo." +
                    "\n- Reporta la situación." +
                    texto_lugar)
            elif problema == "violencia":
                etiqueta_resultado.config(
                    text = "Hola " + nombre +
                    "\nEdad: " + edad +
                    "\n\nPosible situación de violencia." +
                    "\n\nRecomendaciones:" +
                    "\n- Busca ayuda inmediatamente." +
                    "\n- Habla con un adulto de confianza." +
                    texto_lugar)

            elif problema == "discriminacion":
                etiqueta_resultado.config(
                    text = "Hola " + nombre +
                    "\nEdad: " + edad +
                    "\n\nPosible discriminación." +
                    "\n\nRecomendaciones:" +
                    "\n- Reporta la situación." +
                    "\n- Busca apoyo." +
                    texto_lugar)
            else:
                etiqueta_resultado.config(text = "Problema no identificado.")

    def informacion():
        etiqueta_resultado.config(
            text = "Problemas reconocidos:\n\n"
                 "bullying\n"
                 "miedo\n"
                 "tristeza\n"
                 "acoso\n"
                 "violencia\n"
                 "discriminacion\n\n"
                 "Lugares:\n"
                 "escuela\n"
                 "casa\n"
                 "internet\n"
                 "comunidad")
    etiqueta_titulo = Label(ventana_sistema,text = "SISTEMA DE APOYO SOCIAL", font=("Arial",16,"bold"), bg="lightyellow")
    etiqueta_titulo.pack()
    Label(ventana_sistema, text = "Nombre", bg = "lightyellow").pack()
    entrada_nombre = Entry(ventana_sistema)
    entrada_nombre.pack()
    Label(ventana_sistema, text = "Edad", bg = "lightyellow").pack()
    entrada_edad = Entry(ventana_sistema)
    entrada_edad.pack()
    Label(ventana_sistema,text = "Lugar", bg = "lightyellow").pack()
    entrada_lugar = Entry(ventana_sistema)
    entrada_lugar.pack()
    Label(ventana_sistema, text = "Problema", bg = "lightyellow").pack()
    entrada_problema = Entry(ventana_sistema)
    entrada_problema.pack()
    etiqueta_acciones = Label(ventana_sistema, text = "Selecciona una opcion", font = ("Arial", 12, "bold"), bg = "lightyellow")
    etiqueta_acciones.pack(pady = 10)
    boton_analizar = Button(ventana_sistema, text = "Analizar", command = analizar)
    boton_analizar.pack(pady = 5)
    boton_informacion = Button(ventana_sistema, text = "Problemas que reconoce el sistema", command = informacion)
    boton_informacion.pack(pady = 5)
    etiqueta_resultado = Label(ventana_sistema, text = "", bg = "lightyellow")
    etiqueta_resultado.pack()
ventana = Tk()
ventana.title("Bienvenida")
ventana.geometry("500x350")
ventana.configure(bg = "lightblue")
etiqueta_bienvenida = Label(ventana, text = "SISTEMA DE APOYO SOCIAL", font = ("Arial",20,"bold"), bg = "lightblue")
etiqueta_bienvenida.pack(pady = 20)
etiqueta_texto = Label(ventana, text = "Programa para identificar\nproblemas sociales y ofrecer\nrecomendaciones.", font = ("Arial", 12), bg = "lightblue")
etiqueta_texto.pack(pady = 10)
etiqueta_linea = Label(ventana, text = "-----------------------------------", font = ("Arial", 12), bg = "lightblue")
etiqueta_linea.pack()
etiqueta_mensaje = Label(ventana, text = "Presiona el boton para comenzar", font = ("Arial", 11), bg = "lightblue")
etiqueta_mensaje.pack(pady = 10)
boton_entrar = Button(ventana, text = "Entrar al Sistema", font = ("Arial", 14), command = abrir_sistema)
boton_entrar.pack(pady = 15)
ventana.mainloop()
