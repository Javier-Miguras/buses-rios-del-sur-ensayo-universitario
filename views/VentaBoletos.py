from controllers.UsuariosController import UsuariosController
from controllers.TicketSaleController import TicketSaleController
from helpers.validate_helper import validarOpcion
from helpers.validate_helper import cerrarApp

class VentaBoletos:
    def __init__(self, main_menu):
        self.__controller = UsuariosController()
        self.__ticket_sale_controller = TicketSaleController()
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
                    # Validar ruta
                    route = self.__ticket_sale_controller.validateRoute(origen, destino)
                    
                    # Pedir fecha de viaje
                    fecha = input("Ingrese fecha de viaje en formato año-mes-día (Ejemplo: 2024-12-28): ")
                    # Validar viaje

                except Exception as e:
                    print(e)
                continue

                try:
                    if (UsuariosController().create(nombre, rut)):
                        print("Usuario creado correctamente.")
                    else :
                        print("Error al crear usuario.")
                except Exception as e:
                    print(e)
                continue

            elif int(opcion_seleccionada) == 2:
                print(UsuariosController().index())
                continue
                
            elif int(opcion_seleccionada) == 3:
                id = input("Ingrese id de usuario: ")
                nombre = input("Ingrese nombre de usuario: ")
                rut = input("Ingrese Rut de usuario: ")

                try:
                    if (UsuariosController().update(id, nombre, rut)):
                        print("Usuario actualizado correctamente.")
                    else :
                        print("Error al actualizar usuario.")
                except Exception as e:
                    print(e)
                continue

            elif int(opcion_seleccionada) == 4:
                id = input("Ingrese id de usuario: ")

                try:
                    if (UsuariosController().delete(id)):
                        print("Usuario eliminado correctamente.")
                    else :
                        print("Error al eliminar usuario.")
                except Exception as e:
                    print(e)
                continue

            elif int(opcion_seleccionada) == 5:
                self.__main_menu()

            else:
                cerrarApp()