from models.Bus_model import BusModel
from helpers.session_helper import get_session

class BusController:
    def __init__(self):
        self.__bus_model = BusModel()
        

    def index(self):
        usuarios = self.__bus_model.get_all()
        return usuarios
    
    def create(self, modelo, patente, capacidad):
        self.__bus_model.modelo = modelo
        self.__bus_model.patente = patente
        self.__bus_model.capacidad = capacidad

        if self.__bus_model.insert():
            return True
        else:
            return False
    
    def update(self, id, modelo, patente, capacidad):
        try:
            id = int(id)
        except ValueError:
            raise Exception("Error: formato de ID no válido")

        self.__bus_model.id = id
        bus = self.__bus_model.get()

        if not bus:
            raise Exception("Error: Bus no encontrado")

        validate = self.__bus_model.get_all(f"patente = '{patente}' AND id != {id}")

        if validate:
            raise Exception("Error: Patente ya registrada")

        self.__bus_model.modelo = modelo
        self.__bus_model.patente = patente
        self.__bus_model.capacidad = capacidad

        if self.__bus_model.update():
            return True
        else:
            return False

    def delete(self, id):
        try:
            id = int(id)
        except ValueError:
            raise Exception("Error: formato de ID no válido")

        self.__bus_model.id = id
        usuario = self.__bus_model.get()

        if not usuario:
            raise Exception("Error: Bus no encontrado")

        if self.__bus_model.delete():
            return True
        else:
            return False