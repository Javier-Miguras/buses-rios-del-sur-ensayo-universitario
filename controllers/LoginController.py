from models.Usuario_model import UsuarioModel
from helpers.session_helper import set_session

class LoginController:
    def __init__(self):
        self.__usuario_model = UsuarioModel()

    def login(self, username, password):
        validate_username = self.__usuario_model.get_where(f"username = '{username}'")

        if not validate_username:
            raise Exception("Error: Usuario no existe o fue eliminado")
        
        validate_password = self.__usuario_model.get_where(f"username = '{username}' AND password = '{password}'")

        if not validate_password:
            raise Exception("Error: contraseña incorrecta")
        
        self.__usuario_model.id = validate_password[0]
        self.__usuario_model.nombre = validate_password[1]
        self.__usuario_model.rut = validate_password[2] 
        self.__usuario_model.username = validate_password[3]
        self.__usuario_model.email = validate_password[4]
        self.__usuario_model.password = validate_password[5]
        self.__usuario_model.profile_id = validate_password[6] 

        set_session("user", self.__usuario_model)
        return True

    def index(self):
        usuarios = self.__usuario_model.get_all()
        return usuarios
    
    def create(self, nombre, rut):
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