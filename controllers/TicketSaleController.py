from models.Usuario_model import UsuarioModel
from models.Route_model import RouteModel
from models.Travel_model import TravelModel
from models.Sales_model import SalesModel
from models.Ticket_model import TicketModel
from models.Bus_model import BusModel
from pdf.BoletoPDF import BoletoPDF

from fpdf import FPDF
from helpers.session_helper import get_session

class TicketSaleController:
    def __init__(self):
        self.__usuario_model = UsuarioModel()
        self.__route_model = RouteModel()
        self.__travel_model = TravelModel()
        self.__ticket_model = TicketModel()
        self.__bus_model = BusModel()
        self.__boleto_pdf = BoletoPDF()

    def index(self):
        usuarios = self.__usuario_model.get_all()
        return usuarios
    
    def generateTicketPDF(self, code):
        try:
            ticket_data = self.__ticket_model.get_complete_ticket(f"s.code = '{code}'")
            self.__boleto_pdf.generar_pdf(ticket_data)
        except Exception as e:
            print(e)
            return False
    
    def validateRoute(self, origen, destino):
        try:
            route = self.__route_model.get_where(f"origen = '{origen}' AND destino = '{destino}'")
            if not route:
                raise Exception("Error: Ruta no existe o fue eliminada")
            
            return route
        except Exception as e:
            print(e)
            return False

    def validateTravels(self, id_ruta, fecha_salida):
        try:
            travel = self.__travel_model.get_all(f"id_ruta = {id_ruta} AND hora_salida LIKE '{fecha_salida}%'")
            if not travel:
                raise Exception("Error: No hay viajes disponibles para los parámetros ingresados")
            return travel
        except Exception as e:
            print(e)
            return False
        
    def validateTickets(self, id_viaje):
        try:
            tickets = self.__ticket_model.get_all(f"id_viaje = {id_viaje}")
            return tickets
        except Exception as e:
            print(e)
            return False
        
    def validateTravel(self, id_viaje):
        try:
            travel = self.__travel_model.get_where(f"id = {id_viaje}")
            if not travel:
                raise Exception("Error: Viaje no existe o fue eliminado")
            return travel
        except Exception as e:
            print(e)
            return False
        
    def validateBus(self, id_bus):
        try:
            bus = self.__bus_model.get_where(f"id = {id_bus}")
            if not bus:
                raise Exception("Error: Bus no existe o fue eliminado")
            return bus
        except Exception as e:
            print(e)
            return False
        
    def createTicket(self, id_venta, nombre_pasajero, rut_pasajero, id_viaje):
        #TODO: VALIDAR DATOS
        try:
            self.__ticket_model.id_venta = id_venta
            self.__ticket_model.nombre_pasajero = nombre_pasajero
            self.__ticket_model.rut_pasajero = rut_pasajero
            self.__ticket_model.id_viaje = id_viaje

            self.__ticket_model.insert()

        except Exception as e:
            print(e)
            return False
    
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