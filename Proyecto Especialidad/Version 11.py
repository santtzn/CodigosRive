from tkinter import *
from tkinter import messagebox

vidas = 5
puntos = 0
caso_actual = 0
nombre = ""

casos = [
    {
        "situacion":"Carlos recibe burlas todos los dias y tiene miedo de participar en clase.",
        "respuesta":"bullying"
    },
    {
        "situacion":"Una alumna es excluida por su origen y algunos compañeros no quieren trabajar con ella.",
        "respuesta":"discriminacion"
    },
    {
        "situacion":"Un estudiante recibe mensajes ofensivos y amenazas por redes sociales.",
        "respuesta":"ciberacoso"
    },
    {
        "situacion":"Dos alumnos amenazan constantemente a otro estudiante.",
        "respuesta":"violencia"
    },
    {
        "situacion":"Un alumno siempre es dejado fuera de actividades y equipos.",
        "respuesta":"exclusion"
    }
]

def mostrar_caso():

    etiqueta_vidas.config(text="Vidas: " + "❤️" * vidas)
    etiqueta_puntos.config(text="Puntos: " + str(puntos))
    etiqueta_progreso.config(
        text="Caso " + str(caso_actual + 1) + " de 5"
    )

    etiqueta_situacion.config(
        text=casos[caso_actual]["situacion"]
    )

    entrada_respuesta.delete(0, END)

def revisar_respuesta():

    global vidas
    global puntos
    global caso_actual

    respuesta_usuario = entrada_respuesta.get().lower()

    respuesta_correcta = casos[caso_actual]["respuesta"]

    if respuesta_usuario == respuesta_correcta:

        puntos = puntos + 10

        messagebox.showinfo(
            "Correcto",
            "¡Muy bien!\nHas identificado correctamente el problema social."
        )

        caso_actual = caso_actual + 1

        if caso_actual == len(casos):
            victoria()
        else:
            mostrar_caso()

    else:

        vidas = vidas - 1

        if vidas == 0:

            game_over()

        else:

            messagebox.showerror(
                "Incorrecto",
                "Respuesta incorrecta.\nTe quedan " + str(vidas) + " vidas."
            )

            mostrar_caso()

def game_over():

    global vidas
    global puntos
    global caso_actual

    respuesta = messagebox.askyesno(
        "Game Over",
        "Has perdido todas tus vidas.\n\n¿Deseas volver a empezar?"
    )

    if respuesta:

        vidas = 5
        puntos = 0
        caso_actual = 0

        mostrar_caso()

def victoria():

    ventana_victoria = Toplevel()

    ventana_victoria.title("Victoria")
    ventana_victoria.geometry("600x450")

    Label(
        ventana_victoria,
        text="¡FELICIDADES!",
        font=("Arial",20,"bold")
    ).pack(pady=15)

    Label(
        ventana_victoria,
        text="Has ayudado a Alex a resolver todos los casos.",
        font=("Arial",12)
    ).pack()

    Label(
        ventana_victoria,
        text="\nJugador: " + nombre,
        font=("Arial",12)
    ).pack()

    Label(
        ventana_victoria,
        text="Puntos obtenidos: " + str(puntos),
        font=("Arial",12)
    ).pack()

    Label(
        ventana_victoria,
        text=
        "\nProblemas sociales identificados:\n\n"
        "✓ Bullying\n"
        "✓ Discriminacion\n"
        "✓ Ciberacoso\n"
        "✓ Violencia\n"
        "✓ Exclusion",
        font=("Arial",12)
    ).pack(pady=10)

def comenzar_juego():

    global nombre

    nombre = entrada_nombre.get()

    if nombre == "":
        messagebox.showerror(
            "Error",
            "Ingresa tu nombre."
        )
        return

    ventana_inicio.withdraw()

    ventana_juego.deiconify()

    messagebox.showinfo(
        "Alex",
        "Hola " + nombre +
        ".\n\nSoy Alex.\nNecesito tu ayuda para resolver varios casos relacionados con problemas sociales.\n\nDispones de 5 vidas."
    )

    mostrar_caso()

ventana_inicio = Tk()

ventana_inicio.title("Mision Ayuda Social")
ventana_inicio.geometry("700x500")

Label(
    ventana_inicio,
    text="MISION AYUDA SOCIAL",
    font=("Arial",22,"bold")
).pack(pady=20)

Label(
    ventana_inicio,
    text="Ayuda a Alex a resolver casos de problemas sociales.",
    font=("Arial",12)
).pack()

Label(
    ventana_inicio,
    text="\nEscribe tu nombre:"
).pack()

entrada_nombre = Entry(
    ventana_inicio,
    font=("Arial",12)
)
entrada_nombre.pack(pady=10)

Button(
    ventana_inicio,
    text="Comenzar",
    font=("Arial",14),
    command=comenzar_juego
).pack(pady=20)

ventana_juego = Toplevel()

ventana_juego.title("Casos Sociales")
ventana_juego.geometry("800x600")

ventana_juego.withdraw()

etiqueta_vidas = Label(
    ventana_juego,
    text="",
    font=("Arial",14,"bold")
)
etiqueta_vidas.pack(pady=10)

etiqueta_puntos = Label(
    ventana_juego,
    text="",
    font=("Arial",12)
)
etiqueta_puntos.pack()

etiqueta_progreso = Label(
    ventana_juego,
    text="",
    font=("Arial",12)
)
etiqueta_progreso.pack(pady=5)

Label(
    ventana_juego,
    text="CASO",
    font=("Arial",18,"bold")
).pack(pady=10)

etiqueta_situacion = Label(
    ventana_juego,
    text="",
    wraplength=600,
    font=("Arial",12)
)
etiqueta_situacion.pack(pady=20)

Label(
    ventana_juego,
    text="¿Que problema social identificas?",
    font=("Arial",12,"bold")
).pack()

entrada_respuesta = Entry(
    ventana_juego,
    font=("Arial",12),
    width=30
)
entrada_respuesta.pack(pady=10)

Button(
    ventana_juego,
    text="Responder",
    font=("Arial",14),
    command=revisar_respuesta
).pack(pady=20)

ventana_inicio.mainloop()
