from controllers.ReportesController import ReportesController

from helpers.validate_helper import validarOpcion
from helpers.validate_helper import cerrarApp
from helpers.session_helper import get_session

class Reportes:
    def __init__(self, main_menu):
        self.__controller = ReportesController()
        self.__main_menu = main_menu
        self.menu()
        
    def menu(self):
        while True:
            print("""
            ==========================
            Reportería
            ==========================
            1. Reporte de Ventas
            2. Volver al Menú Principal
            0. Salir
            ==========================
            """)

            opcion_seleccionada = input("Seleccione una opción: ")
            
            while not validarOpcion(opcion_seleccionada, 0, 2):
                opcion_seleccionada = input("Opción inválida, vuelva a intentar: ")

            if int(opcion_seleccionada) == 1:
                while True:
                    print("""
                    =============================
                    Generar Reporte de Ventas
                    =============================
                    1. Filtrado por Fecha
                    2. Filtrado por Ruta
                    3. Filtrado por Precio
                    4. Filtrado por Bus
                    5. Volver a Reportería
                    0. Salir
                    =============================
                    """)

                    opcion_seleccionada = input("Seleccione una opción: ")
                    
                    while not validarOpcion(opcion_seleccionada, 0, 5):
                        opcion_seleccionada = input("Opción inválida, vuelva a intentar: ")

                    if int(opcion_seleccionada) == 1:
                        fecha_ini = input("Ingrese fecha de inicio en formato año-mes-día (Ejemplo: 2024-12-28): ")
                        fecha_fin = input("Ingrese fecha de inicio en formato año-mes-día (Ejemplo: 2024-12-28): ")

                        try:
                            self.__controller.reporteVentas(fecha_ini=fecha_ini, fecha_fin=fecha_fin)
                        except Exception as e:
                            print(e)

                    elif int(opcion_seleccionada) == 5:
                        self.menu()

                    else:
                        cerrarApp()

            elif int(opcion_seleccionada) == 2:
                self.__main_menu()

            else:
                cerrarApp()