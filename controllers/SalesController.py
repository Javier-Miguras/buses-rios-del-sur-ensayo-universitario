from models.Usuario_model import UsuarioModel
from models.Route_model import RouteModel
from models.Travel_model import TravelModel
from models.Sales_model import SalesModel
from helpers.session_helper import get_session

class SalesController:
    def __init__(self):
        self.__usuario_model = UsuarioModel()
        self.__route_model = RouteModel()
        self.__travel_model = TravelModel()
        self.__sales_model = SalesModel()

    def index(self):
        usuarios = self.__usuario_model.get_all()
        return usuarios
    
    def getByCode(self, code):
        try:
            sale = self.__sales_model.get_where(f"code = '{code}'")
            if not sale:
                raise Exception("Error: Venta no existe o fue eliminada")
            
            return sale
        except Exception as e:
            print(e)
            return False
    
    def create(self, fecha, id_vendedor, subtotal, iva, total, code):
        self.__sales_model.fecha = fecha
        self.__sales_model.id_vendedor = id_vendedor
        self.__sales_model.subtotal = subtotal
        self.__sales_model.iva = iva
        self.__sales_model.total = total
        self.__sales_model.code = code

        if self.__sales_model.insert():
            print(self.__sales_model.id)
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