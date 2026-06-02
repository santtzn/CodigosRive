from tkinter import *
historial = ""
def abrir_sistema():
    ventana_sistema = Toplevel()
    ventana_sistema.title("Sistema de Apoyo Social")
    ventana_sistema.geometry("700x600")
    ventana_sistema.configure(bg="lightyellow")
    def analizar():
        global historial
        nombre = entrada_nombre.get()
        edad = entrada_edad.get()
        lugar = entrada_lugar.get()
        problema = entrada_problema.get()
        if nombre == "":
            resultado = "Escribe tu nombre."
        elif edad == "":
            resultado = "Escribe tu edad."
        elif lugar == "":
            resultado = "Escribe el lugar."
        elif problema == "":
            resultado = "Escribe el problema."
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
                resultado = (
                    "Hola " + nombre +
                    "\nEdad: " + edad +
                    "\n\nPosible caso de bullying." +
                    "\n\nRecomendaciones:" +
                    "\n- Habla con un maestro." +
                    "\n- Habla con tus padres." +
                    "\n- No respondas con violencia." +
                    texto_lugar)
            elif problema == "miedo":
                resultado = (
                    "Hola " + nombre +
                    "\nEdad: " + edad +
                    "\n\nSituación de miedo." +
                    "\n\nRecomendaciones:" +
                    "\n- Habla con un adulto de confianza." +
                    "\n- Expresa lo que sientes." +
                    texto_lugar)
            elif problema == "tristeza":
                resultado = (
                    "Hola " + nombre +
                    "\nEdad: " + edad +
                    "\n\nPosible problema emocional." +
                    "\n\nRecomendaciones:" +
                    "\n- Habla con alguien de confianza." +
                    "\n- Realiza actividades que disfrutes." +
                    texto_lugar)
            elif problema == "acoso":
                resultado = (
                    "Hola " + nombre +
                    "\nEdad: " + edad +
                    "\n\nPosible acoso." +
                    "\n\nRecomendaciones:" +
                    "\n- Busca apoyo." +
                    "\n- Reporta la situación." +
                    texto_lugar)
            elif problema == "violencia":
                resultado = (
                    "Hola " + nombre +
                    "\nEdad: " + edad +
                    "\n\nPosible situación de violencia." +
                    "\n\nRecomendaciones:" +
                    "\n- Busca ayuda inmediatamente." +
                    "\n- Habla con un adulto de confianza." +
                    texto_lugar)
            elif problema == "discriminacion":
                resultado = (
                    "Hola " + nombre +
                    "\nEdad: " + edad +
                    "\n\nPosible discriminación." +
                    "\n\nRecomendaciones:" +
                    "\n- Reporta la situación." +
                    "\n- Busca apoyo." +
                    texto_lugar)
            else:
                resultado = "Problema no identificado."
        ventana_resultado = Toplevel()
        ventana_resultado.title("Resultado")
        ventana_resultado.geometry("500x400")
        etiqueta_titulo_resultado = Label(
            ventana_resultado,
            text="RESULTADO DEL ANALISIS",
            font=("Arial",16,"bold"))
        etiqueta_titulo_resultado.pack(pady = 10)
        etiqueta_resultado = Label(ventana_resultado, text=resultado)
        etiqueta_resultado.pack(pady=10)
        historial = historial + "\n\n--------------------\n\n" + resultado
    def informacion():
        ventana_info = Toplevel()
        ventana_info.title("Información")
        ventana_info.geometry("400x350")
        etiqueta_info = Label(
            ventana_info, text =
            "Problemas reconocidos:\n\n"
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
        etiqueta_info.pack(pady = 20)
    def ver_historial():
        ventana_historial = Toplevel()
        ventana_historial.title("Historial")
        ventana_historial.geometry("600x400")
        etiqueta_historial = Label(
            ventana_historial,
            text = "HISTORIAL DE CONSULTAS",
            font = ("Arial",16,"bold"))
        etiqueta_historial.pack(pady = 10)
        area_historial = Text(
            ventana_historial,
            width = 60,
            height = 30)
        area_historial.pack()
        area_historial.insert(END, historial)
    etiqueta_titulo = Label(
        ventana_sistema,
        text = "SISTEMA DE APOYO SOCIAL",
        font = ("Arial",16,"bold"),
        bg = "lightyellow")
    etiqueta_titulo.pack()
    Label(
        ventana_sistema,
        text = "Nombre",
        bg = "lightyellow").pack()
    entrada_nombre = Entry(ventana_sistema)
    entrada_nombre.pack()
    Label(
        ventana_sistema,
        text = "Edad",
        bg = "lightyellow").pack()
    entrada_edad = Entry(ventana_sistema)
    entrada_edad.pack()
    Label(
        ventana_sistema,
        text = "Lugar",
        bg = "lightyellow").pack()
    entrada_lugar = Entry(ventana_sistema)
    entrada_lugar.pack()
    Label(
        ventana_sistema,
        text = "Problema",
        bg = "lightyellow").pack()
    entrada_problema = Entry(ventana_sistema)
    entrada_problema.pack()
    etiqueta_acciones = Label(
        ventana_sistema,
        text = "Selecciona una opción",
        font = ("Arial",12,"bold"),
        bg = "lightyellow")
    etiqueta_acciones.pack(pady = 10)
    boton_analizar = Button(
        ventana_sistema, text = "Analizar", command = analizar)
    boton_analizar.pack(pady = 5)
    boton_informacion = Button(
        ventana_sistema, text = "Problemas que reconoce el sistema", command = informacion)
    boton_informacion.pack(pady = 5)
    boton_historial = Button(
        ventana_sistema, text = "Ver Historial", command = ver_historial)
    boton_historial.pack(pady = 5)
ventana = Tk()
ventana.title("Bienvenida")
ventana.geometry("500x350")
ventana.configure(bg = "lightblue")
etiqueta_bienvenida = Label(
    ventana,
    text = "SISTEMA DE APOYO SOCIAL",
    font = ("Arial",20,"bold"),
    bg = "lightblue")
etiqueta_bienvenida.pack(pady = 20)
etiqueta_texto = Label(
    ventana,
    text = "Programa para identificar\nproblemas sociales y ofrecer\nrecomendaciones.",
    font = ("Arial",12),
    bg = "lightblue")
etiqueta_texto.pack(pady=10)
etiqueta_linea = Label(
    ventana,
    text = "-----------------------------------",
    font = ("Arial",12),
    bg = "lightblue")
etiqueta_linea.pack()
etiqueta_mensaje = Label(
    ventana,
    text = "Presiona el botón para comenzar",
    font = ("Arial",11),
    bg = "lightblue")
etiqueta_mensaje.pack(pady=10)
boton_entrar = Button(
    ventana, text = "Entrar al Sistema", font = ("Arial",14), command = abrir_sistema)
boton_entrar.pack(pady=15)
ventana.mainloop()
