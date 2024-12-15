from helpers.validate_helper import validarOpcion
from helpers.validate_helper import cerrarApp

from controllers.LoginController import LoginController
from helpers.session_helper import get_session, clear_session

def main():
    while True:
        print("""
        Bienvenido al Sistema de Gestión
        =============================================
        1. Iniciar Sesión
        0. Salir
        =============================================
        """)

        opcion_seleccionada = input("Seleccione una opción: ")
        
        while not validarOpcion(opcion_seleccionada, 0, 1):
            opcion_seleccionada = input("Opción inválida, vuelva a intentar: ")

        if int(opcion_seleccionada) == 1:
            username = input("Ingrese nombre de usuario: ")
            password = input("Ingrese contraseña: ")

            try:
                if LoginController().login(username, password):
                    print("Sesión iniciada correctamente")
                    user_data = get_session("user")
                    print(user_data.)
                else:
                    print("Error al iniciar sesión")
            except Exception as e:
                print(e)
            continue
        else:
            cerrarApp()

main()
