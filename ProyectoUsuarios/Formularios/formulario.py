from tkinter import Tk, Label, Entry, Button, Text, END, Frame
from Clases.usuarios import Usuarios

class FormularioUsuarios:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Gestión de Usuarios - Modo Programador Pro")
        self.ventana.geometry("600x500")
        self.ventana.configure(bg="#1f2d3d")
        self.fuente = ("Consolas", 12)
        self.usuarios = Usuarios()
        self.crear_interfaz()

    def crear_interfaz(self):
        titulo = Label(self.ventana, text="Gestión de Usuarios", bg="#1f2d3d", fg="#ffffff", font=("Consolas", 18, "bold"))
        titulo.grid(row=0, column=0, columnspan=2, pady=20)
        frame_formulario = Frame(self.ventana, bg="#1f2d3d")
        frame_formulario.grid(row=1, column=0, columnspan=2, padx=20, pady=10)
        self.label_nombre = Label(frame_formulario, text="Nombre:", bg="#1f2d3d", fg="#ffffff", font=self.fuente)
        self.label_nombre.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.entry_nombre = Entry(frame_formulario, bg="#2c3e50", fg="#ffffff", insertbackground="white", font=self.fuente)
        self.entry_nombre.grid(row=0, column=1, padx=10, pady=10)
        self.label_nickname = Label(frame_formulario, text="Nickname:", bg="#1f2d3d", fg="#ffffff", font=self.fuente)
        self.label_nickname.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.entry_nickname = Entry(frame_formulario, bg="#2c3e50", fg="#ffffff", insertbackground="white", font=self.fuente)
        self.entry_nickname.grid(row=1, column=1, padx=10, pady=10)
        self.label_clave = Label(frame_formulario, text="Clave:", bg="#1f2d3d", fg="#ffffff", font=self.fuente)
        self.label_clave.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.entry_clave = Entry(frame_formulario, show="*", bg="#2c3e50", fg="#ffffff", insertbackground="white", font=self.fuente)
        self.entry_clave.grid(row=2, column=1, padx=10, pady=10)
        self.boton_guardar = Button(frame_formulario, text="Guardar", command=self.guardar_usuario, bg="#007acc", fg="#ffffff", font=self.fuente, relief="flat")
        self.boton_guardar.grid(row=3, column=0, padx=10, pady=10)
        self.boton_listar = Button(frame_formulario, text="Listar Usuarios", command=self.listar_usuarios, bg="#1e90ff", fg="#ffffff", font=self.fuente, relief="flat")
        self.boton_listar.grid(row=3, column=1, padx=10, pady=10)
        frame_panel = Frame(self.ventana, bg="#2c3e50")
        frame_panel.grid(row=2, column=0, columnspan=2, padx=20, pady=20)
        self.panel_usuarios = Text(frame_panel, state='disabled', bg="#2c3e50", fg="#ffffff", font=self.fuente, wrap="word", width=60, height=10)
        self.panel_usuarios.pack(padx=10, pady=10)
        self.panel_usuarios.tag_configure("titulo", foreground="#4CAF50", font=("Consolas", 12, "bold"))
        self.panel_usuarios.tag_configure("subtitulo", foreground="#1e90ff", font=("Consolas", 11))
        self.panel_usuarios.tag_configure("texto", foreground="#ffffff", font=("Consolas", 10))
        self.panel_usuarios.tag_configure("linea", foreground="#555555", font=("Consolas", 10))
        self.panel_usuarios.tag_configure("error", foreground="#FF0000", font=("Consolas", 10, "bold"))
        self.panel_usuarios.tag_configure("aviso", foreground="#FFA500", font=("Consolas", 10, "italic"))

    def guardar_usuario(self):
        nombre = self.entry_nombre.get()
        nickname = self.entry_nickname.get()
        clave = self.entry_clave.get()
        if nombre and nickname and clave:
            self.usuarios.guardarUsuario(nombre, nickname, clave)
            self.entry_nombre.delete(0, END)
            self.entry_nickname.delete(0, END)
            self.entry_clave.delete(0, END)
        else:
            self.panel_usuarios.config(state='normal')
            self.panel_usuarios.delete(1.0, END)
            self.panel_usuarios.insert(END, "Error: Todos los campos son obligatorios.\n", "error")
            self.panel_usuarios.config(state='disabled')

    def listar_usuarios(self):
        lista_usuarios = self.usuarios.listarUsuarios()
        self.panel_usuarios.config(state='normal')
        self.panel_usuarios.delete(1.0, END)
        if lista_usuarios:
            for usuario in lista_usuarios:
                self.panel_usuarios.insert(END, f"Nombre: {usuario['nombre']}\n", "titulo")
                self.panel_usuarios.insert(END, f"Nickname: {usuario['nickname']}\n", "subtitulo")
                self.panel_usuarios.insert(END, f"Clave: {usuario['clave']}\n", "texto")
                self.panel_usuarios.insert(END, "-" * 40 + "\n", "linea")
        else:
            self.panel_usuarios.insert(END, "No hay usuarios registrados.\n", "aviso")
        self.panel_usuarios.config(state='disabled')