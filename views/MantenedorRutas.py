from controllers.UsuariosController import UsuariosController
from helpers.validate_helper import validarOpcion
from helpers.validate_helper import cerrarApp

class MantenedorRutas:
    def __init__(self, main_menu):
        self.__controller = UsuariosController()
        self.__main_menu = main_menu
        self.menu()
        
    def menu(self):
        while True:
            print("""
            ==========================
            Mantenedor de Usuarios
            ==========================
            1. Crear una nueva ruta
            2. Ver todas las rutas
            3. Actualizar ruta
            4. Eliminar ruta
            5. Volver al menú principal
            0. Salir
            ==========================
            """)

            opcion_seleccionada = input("Seleccione una opción: ")
            
            while not validarOpcion(opcion_seleccionada, 0, 5):
                opcion_seleccionada = input("Opción inválida, vuelva a intentar: ")

            if int(opcion_seleccionada) == 1:

                origen = input("Ingrese ciudad de origen de nueva ruta: ")
                destino = input("Ingrese ciudad de destino de nueva ruta: ")
                duracion = input("Ingrese tiempo estimado de nueva ruta: ")
                valor = input("Ingrese valor de nueva ruta: ")

                try:
                    if (UsuariosController().create(origen, destino, duracion, valor)):
                        print("Nueva ruta creada correctamente.")
                    else :
                        print("Error al crear nueva ruta.")
                except Exception as e:
                    print(e)
                continue

            elif int(opcion_seleccionada) == 2:
                print(UsuariosController().index())
                continue
                
            elif int(opcion_seleccionada) == 3:
                id = input("Ingrese id de ruta: ")
                origen = input("Ingrese ciudad de origen de ruta: ")
                destino = input("Ingrese ciudad de destino de ruta: ")
                duracion = input("Ingrese tiempo estimado de ruta: ")
                valor = input("Ingrese valor de ruta: ")

                try:
                    if (UsuariosController().update(id, origen, destino, duracion, valor)):
                        print("Ruta actualizada correctamente.")
                    else :
                        print("Error al actualizar usuario ruta.")
                except Exception as e:
                    print(e)
                continue

            elif int(opcion_seleccionada) == 4:
                id = input("Ingrese id de ruta: ")

                try:
                    if (UsuariosController().delete(id)):
                        print("Ruta eliminada correctamente.")
                    else :
                        print("Error al eliminar Ruta.")
                except Exception as e:
                    print(e)
                continue

            elif int(opcion_seleccionada) == 5:
                self.__main_menu()

            else:
                cerrarApp()