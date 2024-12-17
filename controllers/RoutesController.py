from models.Route_model import RouteModel

class RoutesController:
    def __init__(self):
        self.__routes_model = RouteModel()
        

    def index(self):
        usuarios = self.__routes_model.get_all()
        return usuarios
    
    def create(self, origen, destino, duracion, valor):
        self.__routes_model.origen = origen
        self.__routes_model.destino = destino
        self.__routes_model.duracion = duracion
        self.__routes_model.valor = valor        
        

        validate = self.__routes_model.get_where(f"origen = '{origen}' AND destino = '{destino}'")

        if validate:
            raise Exception("Error: La Ruta ya esta creada")
        
        try:
            valor = int(valor)
        except ValueError:
            raise Exception("Error: formato de valor no válido")
        
        try:
            duracion = float(duracion)
        except ValueError:
            raise Exception("Error: formato de duracion no válido")

        if self.__routes_model.insert():
            return True
        else:
            return False
    
    def update(self, id, origen, destino, duracion, valor):
        
        try:
            id = int(id)
        except ValueError:
            raise Exception("Error: formato de ID no válido")

        self.__routes_model.id = id
        usuario = self.__routes_model.get()

        if not usuario:
            raise Exception("Error: Ruta no encontrada")

        validate = self.__routes_model.get_all(f"origen = '{origen}' AND destino = '{destino}'")
        if validate:
            raise Exception("Error: Ruta ya registrado")

        self.__routes_model.origen = origen
        self.__routes_model.destino = destino
        self.__routes_model.duracion = duracion
        self.__routes_model.valor = valor

        if self.__routes_model.update():
            return True
        else:
            return False

    def delete(self, id):
        try:
            id = int(id)
        except ValueError:
            raise Exception("Error: formato de ID no válido")

        self.__routes_model.id = id
        usuario = self.__routes_model.get()

        if not usuario:
            raise Exception("Error: Usuario no encontrado")

        if self.__routes_model.delete():
            return True
        else:
            return False
RoutesController()        