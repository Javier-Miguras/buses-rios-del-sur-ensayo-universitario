from controllers.UsuariosController import UsuariosController
from controllers.TravelController import TravelController

from helpers.validate_helper import validarOpcion
from helpers.validate_helper import cerrarApp

class MantenedorViajes:
    def __init__(self, main_menu):
        self.__controller = TravelController()
        self.__main_menu = main_menu
        self.menu()
        
    def menu(self):
        while True:
            print("""
            ==========================
            Mantenedor de Usuarios
            ==========================
            1. Crear un nuevo viaje
            2. Ver todos los viajes
            3. Actualizar viaje
            4. Eliminar viaje
            5. Volver al menú principal
            0. Salir
            ==========================
            """)

            opcion_seleccionada = input("Seleccione una opción: ")
            
            while not validarOpcion(opcion_seleccionada, 0, 5):
                opcion_seleccionada = input("Opción inválida, vuelva a intentar: ")

            if int(opcion_seleccionada) == 1:

                try:
                    origen = input("Ingrese ciudad de origen: ")
                    destino = input("Ingrese ciudad de destino: ")

                    
                    route = self.__controller.validarRoute(origen, destino)

                    if not route:
                        continue
                    # pedir patente
                    
                    bus = input("Ingrese patende del bus: ")
                    # Validar patente bus
                    validar_bus = self.__controller.validarBus(bus)

                    if not validar_bus:
                        continue
                    
                    fecha_hora_salida = input("Ingrese fecha y hora de salida en el siguiente Formato : dd/mm/YYYY H:M: ")
                    # Validar viajehora fecha
                    validar_fecha_hora_salida = self.__controller.validate_date_time(fecha_hora_salida)

                    if not validar_fecha_hora_salida:
                        continue
                    
                    fecha_hora_llegada = input("Ingrese fecha y hora de llegada en el siguiente Formato : dd/mm/YYYY H:M: ")
                    # Validar viajehora fecha
                    validar_fecha_hora_llegada = self.__controller.validate_date_time(fecha_hora_llegada)

                    if not validar_fecha_hora_llegada:
                        continue
                    
                    # validar chofer
                    rut_chofer = input("ingrese Rut chofer: ")
                    
                    chofer= self.__controller.validarChofer(rut_chofer)

                    if not chofer:
                        continue
                    
                    estado = 1
                    
                    # Crear viaje
                    crear_viaje = self.__controller.create(route[0], bus[0], estado, fecha_hora_salida, fecha_hora_llegada, chofer[0])

                    if not crear_viaje:
                        print("Error al ingresar el viaje")
                        continue
                    
                    
                    
                except Exception as e:
                    print(e)
                continue
    

            elif int(opcion_seleccionada) == 2:
                print(TravelController().index())
                continue
                
            elif int(opcion_seleccionada) == 3:
                id = input("Ingrese id de viaje: ")
                id_ruta = input("Ingrese id Ruta: ")
                id_bus = input("Ingrese id bus: ")
                id_estado = input("Ingrese id de estado de viaje: ")
                hora_salida = input("Ingrese fecha y hora de salida : ")
                hora_llegada = input("Ingrese fecha y hora de llegada: ")
                id_chofer = input("Ingrese id de chofer de usuario: ")

                try:
                    if (TravelController().update(id, id_ruta, id_bus, id_estado, hora_salida, hora_llegada,id_chofer)):
                        print("Viaje actualizado correctamente.")
                    else :
                        print("Error al actualizar usuario.")
                except Exception as e:
                    print(e)
                continue

            elif int(opcion_seleccionada) == 4:
                id = input("Ingrese id de usuario: ")

                try:
                    if (TravelController().delete(id)):
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