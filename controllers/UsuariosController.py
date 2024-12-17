from models.Usuario_model import UsuarioModel

class UsuariosController:
    def __init__(self):
        self.__usuario_model = UsuarioModel()

    def index(self):
        usuarios = self.__usuario_model.get_all()
        return usuarios
    
    def create(self, nombre, rut, username, email, password, profile_id):
        self.__usuario_model.nombre = nombre
        self.__usuario_model.rut = rut

        validate = self.__usuario_model.get_where(f"rut = '{rut}'")

        if validate:
            raise Exception("Error: Usuario ya registrado")

        if self.__usuario_model.insert():
            return True
        else:
            return False
    
    def update(self, id, nombre, rut):
        try:
            id = int(id)
        except ValueError:
            raise Exception("Error: formato de ID no válido")

        self.__usuario_model.id = id
        usuario = self.__usuario_model.get()

        if not usuario:
            raise Exception("Error: Usuario no encontrado")

        validate = self.__usuario_model.get_all(f"rut = '{rut}' AND id != {id}")

        if validate:
            raise Exception("Error: Rut ya registrado")

        self.__usuario_model.nombre = nombre
        self.__usuario_model.rut = rut

        if self.__usuario_model.update():
            return True
        else:
            return False

    def delete(self, id):
        try:
            id = int(id)
        except ValueError:
            raise Exception("Error: formato de ID no válido")

        self.__usuario_model.id = id
        usuario = self.__usuario_model.get()

        if not usuario:
            raise Exception("Error: Usuario no encontrado")

        if self.__usuario_model.delete():
            return True
        else:
            return False