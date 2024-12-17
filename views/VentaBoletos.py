from controllers.UsuariosController import UsuariosController
from controllers.TicketSaleController import TicketSaleController
from controllers.SalesController import SalesController
from helpers.validate_helper import validarOpcion
from helpers.validate_helper import cerrarApp
from helpers.session_helper import get_session
import uuid

class VentaBoletos:
    def __init__(self, main_menu):
        self.__controller = UsuariosController()
        self.__ticket_sale_controller = TicketSaleController()
        self.__sales_controller = SalesController()
        self.__main_menu = main_menu
        self.menu()
        
    def menu(self):
        while True:
            print("""
            ==========================
            Venta de Boletos
            ==========================
            1. Nueva Venta
            2. Cancelar Venta
            3. Volver al Menú Principal
            0. Salir
            ==========================
            """)

            opcion_seleccionada = input("Seleccione una opción: ")
            
            while not validarOpcion(opcion_seleccionada, 0, 3):
                opcion_seleccionada = input("Opción inválida, vuelva a intentar: ")

            if int(opcion_seleccionada) == 1:

                origen = input("Ingrese ciudad de origen: ")
                destino = input("Ingrese ciudad de destino: ")

                try:
                    # Validar perfil usuario

                    # Validar ruta
                    route = self.__ticket_sale_controller.validateRoute(origen, destino)

                    if not route:
                        continue
                    
                    # Pedir fecha de viaje
                    fecha = input("Ingrese fecha de viaje en formato año-mes-día (Ejemplo: 2024-12-28): ")
                    # Validar viaje
                    travels = self.__ticket_sale_controller.validateTravels(route[0], fecha)

                    if not travels:
                        continue

                    for travel in travels:
                        print(f"{travel[0]}. {travel[4]}")

                    travel_id = input("Seleccione horario viaje: ")

                    travel_id = int(travel_id)

                    travel = self.__ticket_sale_controller.validateTravel(travel_id)

                    if not travel:
                        continue

                    # Validar que bus tenga capacidad para agregar un pasajero más  
                    bus = self.__ticket_sale_controller.validateBus(travel[2])

                    if not bus:
                        continue

                    # Contar pasajes del viaje
                    tickets = self.__ticket_sale_controller.validateTickets(travel[0])
                    tickets_count = len(tickets)

                    # Si la cantidad de pasajes comprados es mayor a la capacidad del bus mostrar error
                    if tickets_count >= bus[3]:
                        print("Error: No quedan pasajes disponibles")
                        continue

                    nombre_pasajero = input("Ingrese nombre de pasajero: ")
                    rut_pasajero = input("Ingrese rut de pasajero: ")

                    #Obtener id de usuario logueado
                    user = get_session("user")

                    # Crear código único de venta
                    code = str(uuid.uuid4())

                    # Crear venta
                    iva = 0.19
                    venta_insert = self.__sales_controller.create(fecha, user.id, route[4], route[4]*iva, route[4] + (route[4]*iva), code)

                    if not venta_insert:
                        print("Error al ingresar venta")
                        continue

                    # Obtener objeto venta
                    venta = self.__sales_controller.getByCode(code)

                    # Crear boleto
                    boleto = self.__ticket_sale_controller.createTicket(venta[0], nombre_pasajero, rut_pasajero, travel_id)

                    # Crear PDF boleto
                    self.__ticket_sale_controller.generateTicketPDF(code)

                    print("Boleto creado existosamente")



                except Exception as e:
                    print(e)
                continue

            elif int(opcion_seleccionada) == 2:
                print(UsuariosController().index())
                continue

            elif int(opcion_seleccionada) == 3:
                self.__main_menu()

            else:
                cerrarApp()