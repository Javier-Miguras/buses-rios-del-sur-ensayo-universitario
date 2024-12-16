from views.MantenedorUsuarios import MantenedorUsuarios
from views.MantenedorBuses import MantenedorBuses
from views.VentaBoletos import VentaBoletos
from views.Reportes import Reportes

from helpers.validate_helper import validarOpcion
from helpers.validate_helper import cerrarApp

def menu():
    while True:
        print("""
        =====================================
        Sistema de Gestión Buses Ríos del Sur
        =====================================
        1. Mantenedor Usuarios
        2. Mantenedor Perfiles
        3. Mantenedor Buses
        4. Matener Rutas
        5. Mantenedor Viajes
        6. Venta de Boletos
        7. Reportería
        0. Salir
        =====================================
        """)

        opcion_seleccionada = input("Seleccione una opción: ")
        
        while not validarOpcion(opcion_seleccionada, 0, 7):
            opcion_seleccionada = input("Opción inválida, vuelva a intentar: ")

        if int(opcion_seleccionada) == 1:
            mantenedor_usuarios = MantenedorUsuarios(main_menu=menu)
            mantenedor_usuarios.menu()

        # elif int(opcion_seleccionada) == 2:

        elif int(opcion_seleccionada) == 3:
            martenedor_buses = MantenedorBuses(main_menu=menu)
            martenedor_buses.menu()


        # elif int(opcion_seleccionada) == 4:

        # elif int(opcion_seleccionada) == 5:

        elif int(opcion_seleccionada) == 6:
            venta_boletos = VentaBoletos(main_menu=menu)
            venta_boletos.menu()

        elif int(opcion_seleccionada) == 7:
            reportes = Reportes(main_menu=menu)
            reportes.menu()
        else:
            cerrarApp()