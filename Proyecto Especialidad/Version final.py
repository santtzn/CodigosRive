from tkinter import *
from tkinter import ttk
from tkinter import messagebox

nombre_usuario = ""
mejor_puntaje_juego = 0
mejor_calificacion = 0
historial = []

ventana = Tk()

ventana.title(
    "Identificador de Problemas Sociales"
)

ventana.geometry(
    "1100x700"
)

ventana.resizable(
    False,
    False
)

ventana.configure(
    bg="#1E3A5F"
)

encabezado = Frame(
    ventana,
    bg="#16304D",
    height=120
)

encabezado.pack(
    fill="x"
)

titulo = Label(
    encabezado,
    text="IDENTIFICADOR DE PROBLEMAS SOCIALES",
    font=("Arial", 26, "bold"),
    fg="white",
    bg="#16304D"
)

titulo.pack(
    pady=15
)

subtitulo = Label(
    encabezado,
    text="Proyecto interactivo para el aprendizaje y reconocimiento de problemáticas sociales",
    font=("Arial", 11),
    fg="white",
    bg="#16304D"
)

subtitulo.pack()

contenedor = Frame(
    ventana,
    bg="white"
)

contenedor.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=20
)

marco_registro = LabelFrame(
    contenedor,
    text="Registro de Usuario",
    font=("Arial", 12, "bold"),
    padx=20,
    pady=20,
    bg="white"
)

marco_registro.pack(
    fill="x",
    padx=20,
    pady=10
)

Label(
    marco_registro,
    text="Nombre del estudiante:",
    font=("Arial", 11),
    bg="white"
).grid(
    row=0,
    column=0,
    padx=10,
    pady=10
)

entrada_nombre = Entry(
    marco_registro,
    font=("Arial", 11),
    width=30
)

entrada_nombre.grid(
    row=0,
    column=1,
    padx=10
)

etiqueta_usuario = Label(
    marco_registro,
    text="Sin registrar",
    font=("Arial", 11, "bold"),
    fg="red",
    bg="white"
)

etiqueta_usuario.grid(
    row=0,
    column=2,
    padx=20
)

def ingresar():

    global nombre_usuario

    nombre_usuario = entrada_nombre.get()

    if nombre_usuario == "":

        messagebox.showerror(
            "Error",
            "Debes ingresar tu nombre."
        )

        return

    etiqueta_usuario.config(
        text="Usuario: " + nombre_usuario,
        fg="green"
    )
    
def abrir_problematicas():

    ventana_problemas = Toplevel()

    ventana_problemas.title(
        "Problemáticas Sociales"
    )

    ventana_problemas.geometry(
        "900x600"
    )

    ventana_problemas.configure(
        bg="#F5F7FA"
    )

    titulo = Label(
        ventana_problemas,
        text="PROBLEMÁTICAS SOCIALES",
        font=("Arial",22,"bold"),
        bg="#F5F7FA",
        fg="#16304D"
    )

    titulo.pack(
        pady=20
    )

    texto_info = Text(
        ventana_problemas,
        width=80,
        height=18,
        font=("Arial",11)
    )

    texto_info.pack(
        pady=20
    )

    def mostrar_bullying():

        texto_info.delete(
            "1.0",
            END
        )

        texto_info.insert(
            END,
            """BULLYING

Descripción:
El bullying es una forma de acoso repetitivo que una persona ejerce sobre otra con la intención de causar daño físico o emocional.

Ejemplos:
• Burlas constantes.
• Apodos ofensivos.
• Humillaciones.

Consecuencias:
• Baja autoestima.
• Ansiedad.
• Tristeza.

Prevención:
• Informar a un adulto.
• Fomentar el respeto.
• No participar en agresiones.
"""
        )

    def mostrar_discriminacion():

        texto_info.delete(
            "1.0",
            END
        )

        texto_info.insert(
            END,
            """DISCRIMINACIÓN

Descripción:
Ocurre cuando una persona recibe un trato injusto por sus características personales.

Ejemplos:
• Rechazo por origen.
• Burlas por apariencia.
• Exclusión por diferencias.

Consecuencias:
• Inseguridad.
• Aislamiento.
• Baja autoestima.

Prevención:
• Respetar las diferencias.
• Promover la igualdad.
• Evitar prejuicios.
"""
        )

    def mostrar_ciberacoso():

        texto_info.delete(
            "1.0",
            END
        )

        texto_info.insert(
            END,
            """CIBERACOSO

Descripción:
Es el acoso realizado mediante internet, redes sociales o aplicaciones de mensajería.

Ejemplos:
• Mensajes ofensivos.
• Amenazas.
• Difusión de rumores.

Consecuencias:
• Estrés.
• Ansiedad.
• Problemas emocionales.

Prevención:
• Configurar privacidad.
• Bloquear agresores.
• Reportar contenido dañino.
"""
        )

    def mostrar_violencia():

        texto_info.delete(
            "1.0",
            END
        )

        texto_info.insert(
            END,
            """VIOLENCIA

Descripción:
La violencia consiste en acciones que dañan física o emocionalmente a una persona.

Ejemplos:
• Golpes.
• Empujones.
• Amenazas.

Consecuencias:
• Lesiones.
• Miedo.
• Problemas psicológicos.

Prevención:
• Resolver conflictos mediante diálogo.
• Buscar ayuda.
• Denunciar agresiones.
"""
        )

    def mostrar_exclusion():

        texto_info.delete(
            "1.0",
            END
        )

        texto_info.insert(
            END,
            """EXCLUSIÓN

Descripción:
La exclusión ocurre cuando una persona es apartada o ignorada dentro de un grupo.

Ejemplos:
• No permitir participar.
• Ignorar a alguien.
• Dejar fuera de equipos.

Consecuencias:
• Soledad.
• Baja autoestima.
• Sentimiento de rechazo.

Prevención:
• Incluir a todos.
• Fomentar el compañerismo.
• Respetar las diferencias.
"""
        )

    Frame(
        ventana_problemas,
        bg="#F5F7FA"
    ).pack()

    Button(
        ventana_problemas,
        text="Bullying",
        width=18,
        command=mostrar_bullying
    ).pack(pady=3)

    Button(
        ventana_problemas,
        text="Discriminación",
        width=18,
        command=mostrar_discriminacion
    ).pack(pady=3)

    Button(
        ventana_problemas,
        text="Ciberacoso",
        width=18,
        command=mostrar_ciberacoso
    ).pack(pady=3)

    Button(
        ventana_problemas,
        text="Violencia",
        width=18,
        command=mostrar_violencia
    ).pack(pady=3)

    Button(
        ventana_problemas,
        text="Exclusión",
        width=18,
        command=mostrar_exclusion
    ).pack(pady=3)

    Button(
        ventana_problemas,
        text="Cerrar",
        width=18,
        command=ventana_problemas.destroy
    ).pack(
        pady=10
    )

def abrir_evaluacion():

    if nombre_usuario == "":
        messagebox.showerror(
            "Acceso denegado",
            "Primero necesitas registrarte."
        )
        return

    ventana_eval = Toplevel()

    ventana_eval.title(
        "Evaluación Social"
    )

    ventana_eval.geometry(
        "900x650"
    )

    ventana_eval.configure(
        bg="#F5F7FA"
    )

    preguntas = [

        {
            "pregunta":
            "Durante varias semanas, un estudiante ha recibido mensajes ofensivos por redes sociales de manera constante.\n\n¿Cuál de las siguientes opciones describe mejor esta situación?",

            "opciones":
            [
                "Es una forma de ciberacoso.",
                "Es una actividad recreativa.",
                "Es una forma de inclusión."
            ],

            "correcta":0
        },

        {
            "pregunta":
            "Un grupo de estudiantes se niega a trabajar con una compañera debido a su lugar de origen.\n\n¿Qué problema social se presenta?",

            "opciones":
            [
                "Violencia",
                "Discriminación",
                "Ciberacoso"
            ],

            "correcta":1
        },

        {
            "pregunta":
            "Un alumno recibe apodos ofensivos todos los días durante el recreo.\n\n¿Qué situación describe mejor el caso?",

            "opciones":
            [
                "Exclusión",
                "Bullying",
                "Inclusión"
            ],

            "correcta":1
        },

        {
            "pregunta":
            "Durante una actividad deportiva, un estudiante es apartado de todos los equipos.\n\n¿Qué problema social se observa?",

            "opciones":
            [
                "Exclusión",
                "Discriminación",
                "Violencia"
            ],

            "correcta":0
        },

        {
            "pregunta":
            "Dos estudiantes golpean a otro compañero para intimidarlo.\n\n¿Qué representa esta situación?",

            "opciones":
            [
                "Violencia",
                "Ciberacoso",
                "Exclusión"
            ],

            "correcta":0
        },

        {
            "pregunta":
            "Compartir fotografías de una persona sin permiso para burlarse de ella es un ejemplo de:",

            "opciones":
            [
                "Respeto",
                "Ciberacoso",
                "Inclusión"
            ],

            "correcta":1
        },

        {
            "pregunta":
            "Tratar injustamente a una persona por su apariencia física es:",

            "opciones":
            [
                "Discriminación",
                "Ayuda",
                "Compañerismo"
            ],

            "correcta":0
        },

        {
            "pregunta":
            "Ignorar constantemente a un compañero y no permitirle participar corresponde a:",

            "opciones":
            [
                "Exclusión",
                "Apoyo",
                "Solidaridad"
            ],

            "correcta":0
        },

        {
            "pregunta":
            "Amenazar físicamente a otra persona es un ejemplo de:",

            "opciones":
            [
                "Inclusión",
                "Violencia",
                "Respeto"
            ],

            "correcta":1
        },

        {
            "pregunta":
            "¿Qué acción ayuda a prevenir los problemas sociales?",

            "opciones":
            [
                "Respetar a los demás",
                "Participar en burlas",
                "Excluir compañeros"
            ],

            "correcta":0
        }

    ]

    pregunta_actual = 0
    puntos = 0

    titulo = Label(
        ventana_eval,
        text="EVALUACIÓN SOCIAL",
        font=("Arial",20,"bold"),
        bg="#F5F7FA"
    )

    titulo.pack(pady=15)

    progreso = Label(
        ventana_eval,
        text="Pregunta 1 de 10",
        font=("Arial",12,"bold"),
        bg="#F5F7FA"
    )

    progreso.pack()

    barra = ttk.Progressbar(
        ventana_eval,
        length=500,
        maximum=10
    )

    barra.pack(pady=10)

    texto_pregunta = Label(
        ventana_eval,
        text="",
        wraplength=700,
        font=("Arial",12),
        bg="white",
        relief="solid",
        padx=20,
        pady=20
    )

    texto_pregunta.pack(
        pady=20,
        padx=20,
        fill="x"
    )

    def mostrar_pregunta():

        progreso.config(
            text="Pregunta " +
            str(pregunta_actual + 1) +
            " de 10"
        )

        barra["value"] = pregunta_actual

        texto_pregunta.config(
            text=preguntas[pregunta_actual]["pregunta"]
        )

        boton_a.config(
            text="A) " +
            preguntas[pregunta_actual]["opciones"][0]
        )

        boton_b.config(
            text="B) " +
            preguntas[pregunta_actual]["opciones"][1]
        )

        boton_c.config(
            text="C) " +
            preguntas[pregunta_actual]["opciones"][2]
        )

    def responder(opcion):

        nonlocal pregunta_actual
        nonlocal puntos

        if opcion == preguntas[pregunta_actual]["correcta"]:

            puntos += 10

        pregunta_actual += 1

        if pregunta_actual >= len(preguntas):

            finalizar()
            return

        mostrar_pregunta()

    def finalizar():

        calificacion = puntos

        global mejor_calificacion

        if calificacion > mejor_calificacion:

            mejor_calificacion = calificacion

        historial.append(
            nombre_usuario +
            " - Evaluación: " +
            str(calificacion) +
            "%"
        )

        if calificacion >= 80:

            resultado = "Excelente"

        elif calificacion >= 60:

            resultado = "Bueno"

        else:

            resultado = (
                "Necesita mejorar\n\n"
                "Te recomendamos revisar la sección de Problemáticas Sociales."
            )

        messagebox.showinfo(
            "Resultado Final",
            "Calificación: "
            + str(calificacion)
            + "%\n\n"
            + resultado
        )

        ventana_eval.destroy()

    boton_a = Button(
        ventana_eval,
        width=50,
        height=2,
        command=lambda: responder(0)
    )

    boton_a.pack(pady=5)

    boton_b = Button(
        ventana_eval,
        width=50,
        height=2,
        command=lambda: responder(1)
    )

    boton_b.pack(pady=5)

    boton_c = Button(
        ventana_eval,
        width=50,
        height=2,
        command=lambda: responder(2)
    )

    boton_c.pack(pady=5)

    mostrar_pregunta()

def abrir_juego():

    if nombre_usuario == "":
        messagebox.showerror(
            "Acceso denegado",
            "Primero necesitas registrarte."
        )
        return

    ventana_juego = Toplevel()

    ventana_juego.title(
        "Clasificador de Casos"
    )

    ventana_juego.geometry(
        "900x650"
    )

    ventana_juego.configure(
        bg="#F5F7FA"
    )

    casos = [

        {
            "caso":
            "Carlos recibe burlas constantes por parte de varios compañeros. Todos los días le ponen apodos ofensivos y se ríen cuando participa en clase.",

            "correcta":"Bullying"
        },

        {
            "caso":
            "Una alumna no es aceptada en los equipos de trabajo debido a su lugar de origen. Algunos estudiantes dicen que no quieren trabajar con ella por ser diferente.",

            "correcta":"Discriminación"
        },

        {
            "caso":
            "Un estudiante recibe mensajes ofensivos, amenazas y burlas mediante redes sociales después del horario escolar.",

            "correcta":"Ciberacoso"
        },

        {
            "caso":
            "Dos alumnos empujan y golpean repetidamente a otro estudiante durante el recreo para intimidarlo.",

            "correcta":"Violencia"
        },

        {
            "caso":
            "Un compañero siempre es ignorado en actividades escolares y nunca es elegido para participar en equipos o dinámicas.",

            "correcta":"Exclusión"
        }

    ]

    vidas = 3
    puntos = 0
    caso_actual = 0

    titulo = Label(
        ventana_juego,
        text="CLASIFICADOR DE CASOS",
        font=("Arial",20,"bold"),
        bg="#F5F7FA"
    )

    titulo.pack(pady=15)

    etiqueta_vidas = Label(
        ventana_juego,
        text="❤️❤️❤️",
        font=("Arial",14,"bold"),
        bg="#F5F7FA"
    )

    etiqueta_vidas.pack()

    etiqueta_puntos = Label(
        ventana_juego,
        text="Puntos: 0",
        font=("Arial",12,"bold"),
        bg="#F5F7FA"
    )

    etiqueta_puntos.pack()

    barra = ttk.Progressbar(
        ventana_juego,
        length=500,
        maximum=5
    )

    barra.pack(
        pady=10
    )

    progreso = Label(
        ventana_juego,
        text="Caso 1 de 5",
        font=("Arial",12,"bold"),
        bg="#F5F7FA"
    )

    progreso.pack()

    texto_caso = Label(
        ventana_juego,
        text="",
        wraplength=700,
        font=("Arial",12),
        bg="white",
        relief="solid",
        padx=20,
        pady=20
    )

    texto_caso.pack(
        padx=20,
        pady=20,
        fill="x"
    )

    def mostrar_caso():

        texto_caso.config(
            text=casos[caso_actual]["caso"]
        )

        progreso.config(
            text="Caso " +
            str(caso_actual + 1) +
            " de 5"
        )

        barra["value"] = caso_actual

        etiqueta_vidas.config(
            text="❤️" * vidas
        )

        etiqueta_puntos.config(
            text="Puntos: " + str(puntos)
        )

    def responder(respuesta):

        nonlocal vidas
        nonlocal puntos
        nonlocal caso_actual

        if respuesta == casos[caso_actual]["correcta"]:

            puntos += 20

        else:

            vidas -= 1

        caso_actual += 1

        if vidas <= 0:

            historial.append(
                nombre_usuario +
                " - Juego: " +
                str(puntos) +
                " puntos"
            )

            messagebox.showwarning(
                "Juego terminado",
                "Te quedaste sin vidas.\n\nPuntaje final: "
                + str(puntos)
            )

            ventana_juego.destroy()
            return

        if caso_actual >= len(casos):

            global mejor_puntaje_juego
            
            if puntos > mejor_puntaje_juego:
                
                mejor_puntaje_juego = puntos
                
            historial.append(
                nombre_usuario +
                " - Juego: " +
                str(puntos) +
                " puntos"
            )

            messagebox.showinfo(
                "Felicidades",
                "Has completado todos los casos.\n\nPuntaje final: "
                + str(puntos)
            )

            ventana_juego.destroy()
            return

        mostrar_caso()

    Button(
        ventana_juego,
        text="Bullying",
        width=25,
        command=lambda: responder("Bullying")
    ).pack(pady=3)

    Button(
        ventana_juego,
        text="Discriminación",
        width=25,
        command=lambda: responder("Discriminación")
    ).pack(pady=3)

    Button(
        ventana_juego,
        text="Ciberacoso",
        width=25,
        command=lambda: responder("Ciberacoso")
    ).pack(pady=3)

    Button(
        ventana_juego,
        text="Violencia",
        width=25,
        command=lambda: responder("Violencia")
    ).pack(pady=3)

    Button(
        ventana_juego,
        text="Exclusión",
        width=25,
        command=lambda: responder("Exclusión")
    ).pack(pady=3)

    mostrar_caso()
    
menu_frame = LabelFrame(
    contenedor,
    text="Menú Principal",
    font=("Arial", 12, "bold"),
    padx=30,
    pady=30,
    bg="white"
)

def abrir_estadisticas():

    if nombre_usuario == "":

        messagebox.showerror(
            "Acceso denegado",
            "Primero debes registrar tu nombre."
        )

        return

    ventana_estadisticas = Toplevel()

    ventana_estadisticas.title(
        "Estadísticas"
    )

    ventana_estadisticas.geometry(
        "900x600"
    )

    ventana_estadisticas.configure(
        bg="#F5F7FA"
    )

    Label(
        ventana_estadisticas,
        text="ESTADÍSTICAS DEL USUARIO",
        font=("Arial",22,"bold"),
        bg="#F5F7FA",
        fg="#16304D"
    ).pack(
        pady=20
    )

    Label(
        ventana_estadisticas,
        text="Usuario: " + nombre_usuario,
        font=("Arial",14,"bold"),
        bg="#F5F7FA"
    ).pack(
        pady=10
    )

    Label(
        ventana_estadisticas,
        text="Mejor puntuación en el juego: "
        + str(mejor_puntaje_juego),
        font=("Arial",12),
        bg="#F5F7FA"
    ).pack(
        pady=5
    )

    Label(
        ventana_estadisticas,
        text="Mejor calificación en evaluación: "
        + str(mejor_calificacion)
        + "%",
        font=("Arial",12),
        bg="#F5F7FA"
    ).pack(
        pady=5
    )

    Label(
        ventana_estadisticas,
        text="Historial",
        font=("Arial",16,"bold"),
        bg="#F5F7FA"
    ).pack(
        pady=20
    )

    lista = Listbox(
        ventana_estadisticas,
        width=80,
        height=12,
        font=("Arial",11)
    )

    lista.pack(
        pady=10
    )

    for dato in historial:

        lista.insert(
            END,
            dato
        )

    Button(
        ventana_estadisticas,
        text="Cerrar",
        width=20,
        command=ventana_estadisticas.destroy
    ).pack(
        pady=15
    )

menu_frame.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=20
)

Button(
    menu_frame,
    text="Registrar Usuario",
    width=30,
    height=2,
    font=("Arial",11,"bold"),
    command=ingresar
).pack(pady=10)

Button(
    menu_frame,
    text="Problemáticas Sociales",
    width=30,
    height=2,
    font=("Arial",11,"bold"),
    command=abrir_problematicas
).pack(pady=10)

Button(
    menu_frame,
    text="Evaluación Social",
    width=30,
    height=2,
    font=("Arial",11,"bold"),
    command=abrir_evaluacion
).pack(pady=10)

Button(
    menu_frame,
    text="Clasificador de Casos",
    width=30,
    height=2,
    font=("Arial",11,"bold"),
    command=abrir_juego
).pack(pady=10)

Button(
    menu_frame,
    text="Estadísticas",
    width=30,
    height=2,
    font=("Arial",11,"bold"),
    command=abrir_estadisticas
).pack(pady=10)

Button(
    menu_frame,
    text="Salir",
    width=30,
    height=2,
    font=("Arial",11,"bold"),
    command=ventana.destroy
).pack(pady=10)

ventana.mainloop()
