from views.MantenedorUsuarios import MantenedorUsuarios
from views.MantenedorBuses import MantenedorBuses
from views.VentaBoletos import VentaBoletos
from views.MantenedorRutas import MantenedorRutas
from views.MantenedorViajes import MantenedorViajes
from views.Reportes import Reportes

from helpers.session_helper import get_session
from helpers.validate_helper import validarOpcion
from helpers.validate_helper import cerrarApp

def menu():

    user_data = get_session("user")

    while True:
        print(f"""
        =====================================
        Sistema de Gestión Buses Ríos del Sur
              
        Bienvenido otra vez {user_data.nombre}!
        =====================================
        1. Mantenedor Usuarios
        2. Mantenedor Buses
        3. Matener Rutas
        4. Mantenedor Viajes
        5. Venta de Boletos
        6. Reportería
        0. Salir
        =====================================
        """)

        opcion_seleccionada = input("Seleccione una opción: ")
        
        while not validarOpcion(opcion_seleccionada, 0, 6):
            opcion_seleccionada = input("Opción inválida, vuelva a intentar: ")

        if int(opcion_seleccionada) == 1:
            mantenedor_usuarios = MantenedorUsuarios(main_menu=menu)
            mantenedor_usuarios.menu()

        elif int(opcion_seleccionada) == 2:
            martenedor_buses = MantenedorBuses(main_menu=menu)
            martenedor_buses.menu()


        elif int(opcion_seleccionada) == 3:
            mantenedor_rutas = MantenedorRutas(main_menu=menu)
            mantenedor_rutas.menu()

        elif int(opcion_seleccionada) == 4:
            mantenedor_viaje = MantenedorViajes(main_menu=menu)
            mantenedor_viaje.menu()

        elif int(opcion_seleccionada) == 5:
            venta_boletos = VentaBoletos(main_menu=menu)
            venta_boletos.menu()

        elif int(opcion_seleccionada) == 6:
            reportes = Reportes(main_menu=menu)
            reportes.menu()
        else:
            cerrarApp()