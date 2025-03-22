class Usuarios:
    def __init__(self):
        self.lista_usuarios = []

    def guardarUsuario(self, nombre, nickname, clave):
        usuario = {
            'nombre': nombre,
            'nickname': nickname,
            'clave': clave
        }
        self.lista_usuarios.append(usuario)

    def listarUsuarios(self):
        return self.lista_usuarios