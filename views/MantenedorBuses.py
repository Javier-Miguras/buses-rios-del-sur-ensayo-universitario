from controllers.BusController import BusController
from helpers.validate_helper import validarOpcion
from helpers.validate_helper import cerrarApp

class MantenedorBuses:
    def __init__(self, main_menu):
        self.__controller = BusController()
        self.__main_menu = main_menu
        self.menu()
        
    def menu(self):
        while True:
            print("""
            ==========================
            Mantenedor de Usuarios
            ==========================
            1. Crear un nuevo bus
            2. Ver todos los buses
            3. Actualizar bus
            4. Eliminar bus
            5. Volver al menú principal
            0. Salir
            ==========================
            """)

            opcion_seleccionada = input("Seleccione una opción: ")
            
            while not validarOpcion(opcion_seleccionada, 0, 5):
                opcion_seleccionada = input("Opción inválida, vuelva a intentar: ")

            if int(opcion_seleccionada) == 1:

                modelo = input("Ingrese modelo del bus: ")
                patente = input("Ingrese patente del bus: ")
                capacidad = input("Ingrese capacidad del bus: ")

                try:
                    if (BusController().create(modelo, patente, capacidad)):
                        print("Nuevo bus crado correctamente.")
                    else :
                        print("Error al crear el nuevo bus.")
                except Exception as e:
                    print(e)
                continue

            elif int(opcion_seleccionada) == 2:
                print(BusController().index())
                continue
                
            elif int(opcion_seleccionada) == 3:
                id = input("Ingrese id de bus: ")
                modelo = input("Ingrese modelo del bus: ")
                patente = input("Ingrese patente del bus: ")
                capacidad = input("Ingrese capacidad del bus: ")

                try:
                    if (BusController().update(id, modelo, patente, capacidad)):
                        print("Bus actualizado correctamente.")
                    else :
                        print("Error al actualizar el bus.")
                except Exception as e:
                    print(e)
                continue

            elif int(opcion_seleccionada) == 4:
                id = input("Ingrese id de bus: ")

                try:
                    if (BusController().delete(id)):
                        print("Bus eliminado correctamente.")
                    else :
                        print("Error al eliminar bus.")
                except Exception as e:
                    print(e)
                continue

            elif int(opcion_seleccionada) == 5:
                self.__main_menu()

            else:
                cerrarApp()