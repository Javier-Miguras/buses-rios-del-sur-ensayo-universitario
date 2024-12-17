from models.Travel_model import TravelModel
from models.Bus_model import BusModel
from models.Route_model import RouteModel
from models.Usuario_model import UsuarioModel
from datetime import datetime

class TravelController:
    def __init__(self):
        self.__travel_model = TravelModel()
        self.__bus_model = BusModel()
        self.__route_model = RouteModel()
        self.__usuario_model = UsuarioModel()

    def index(self):
        usuarios = self.__travel_model.get_all()
        return usuarios
    
    def validarRoute(self, origen, destino):
        try:
            route = self.__route_model.get_where(f"origen = '{origen}' AND destino = '{destino}'")
            if not route:
                raise Exception("Error: Ruta no existe o fue eliminada")
            
            return route
        except Exception as e:
            print(e)
            return False
        
    def validarBus(self, patente):
        try:
            bus = self.__bus_model.get_where(f"patente = {patente}")
            if not bus:
                raise Exception("Error: Bus no existe o fue eliminado")
            return bus
        except Exception as e:
            print(e)
            return False 
        
    def validarChofer(self, rut):
        try:
            chofer = self.__usuario_model.get_where(f"rut = '{rut}', AND profile_id = 3")
            if not chofer:
                raise Exception("Error: Chofer no existe o fue eliminado")
            return chofer
        except Exception as e:
            print(e)
            return False 
        
    def validate_date_time(fecha_hora_salida, formato="%d/%m/%Y %H:%M"):
        try:
        # Intentar convertir la fecha y hora al formato especificado
            fecha_hora = datetime.strptime(fecha_hora, formato)
            if not fecha_hora:
                raise Exception("Error: Formatop de fecha y hora no validas")
            return fecha_hora
        except Exception as e:
            print(e)
            return False              
    
    def create(self, id_ruta, id_bus, id_estado, hora_salida, hora_llegada, id_chofer):
        self.__travel_model.id_ruta = id_ruta
        self.__travel_model.id_bus = id_bus
        self.__travel_model.id_estado = id_estado
        self.__travel_model.hora_salida = hora_salida
        self.__travel_model.hora_llegada = hora_llegada
        self.__travel_model.id_chofer = id_chofer

        validate = self.__travel_model.get_where(f"id_ruta = '{id_ruta}', AND hora_salida = {hora_salida}")

        if validate:
            raise Exception("Error: viaje ya registrado")

        if self.__travel_model.insert():
            return True
        else:
            return False
    
    def update(self, id, id_ruta, id_bus, id_estado, hora_salida, hora_llegada, id_chofer):
        try:
            id = int(id)
        except ValueError:
            raise Exception("Error: formato de ID no válido")

        self.__travel_model.id = id
        usuario = self.__travel_model.get()

        if not usuario:
            raise Exception("Error: Usuario no encontrado")

        validate = self.__travel_model.get_all(f"id_ruta = '{id_ruta}' AND id != {id}")

        if validate:
            raise Exception("Error: viaje ya registrado")

        self.__travel_model.id_ruta = id_ruta
        self.__travel_model.id_bus = id_bus
        self.__travel_model.id_estado = id_estado
        self.__travel_model.hora_salida = hora_salida
        self.__travel_model.hora_llegada = hora_llegada
        self.__travel_model.id_chofer = id_chofer

        if self.__travel_model.update():
            return True
        else:
            return False

    def delete(self, id):
        try:
            id = int(id)
        except ValueError:
            raise Exception("Error: formato de ID no válido")

        self.__travel_model.id = id
        usuario = self.__travel_model.get()

        if not usuario:
            raise Exception("Error: Usuario no encontrado")

        if self.__travel_model.delete():
            return True
        else:
            return False