from views.MantenedorUsuarios import MantenedorUsuarios

from helpers.validate_helper import validarOpcion
from helpers.validate_helper import cerrarApp

def main():
    print("""
        Bienvenido al Sistema de Gestión
        =============================================
        1. Mantenedor de Usuarios
        2. Mantenedor de Cuentas Corrientes
        3. Mantenedor de Tipos de Movimientos
        4. Menú de Transacciones (Cuentas Corrientes)
        5. Ver Reportes Generales
        6. Configuración del Sistema
        0. Salir
        =============================================
    """)

    opcion_seleccionada = input("Seleccione una opción: ")
    
    while not validarOpcion(opcion_seleccionada, 0, 6):
        opcion_seleccionada = input("Opción inválida, vuelva a intentar: ")

    if int(opcion_seleccionada) == 1:
        mantenedorUsuarios = MantenedorUsuarios(main_menu=main)
        mantenedorUsuarios.menu()
    # elif int(opcion_seleccionada) == 2:

    # elif int(opcion_seleccionada) == 3:

    # elif int(opcion_seleccionada) == 4:

    # elif int(opcion_seleccionada) == 5:

    # elif int(opcion_seleccionada) == 6:

    else:
        cerrarApp()

main()
