import sqlite3

class RouteModel:
    def __init__(self):
        self.__conn = sqlite3.connect("trabajo.db")
        self.__id = None
        self.__origen = None
        self.__destino = None
        self.__duracion = None
        self.__valor = None
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def origen(self):
        return self.__origen

    @origen.setter
    def origen(self, value):
        self.__origen = value

    @property
    def destino(self):
        return self.__destino

    @destino.setter
    def destino(self, value):
        self.__destino = value

    @property
    def duracion(self):
        return self.__duracion

    @duracion.setter
    def duracion(self, value):
        self.__duracion = value
        
    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, value):
        self.__valor = value       

    def get(self):
        query = self.__conn.execute(f"SELECT * FROM routes WHERE id = {self.id}")
        data = query.fetchone()
        return data

    def get_where(self, where=''):
        if where == '':
            where = '1 > 0'
        try:
            query = self.__conn.execute(f"SELECT * FROM routes WHERE {where}")
            data = query.fetchone()
            return data
        except sqlite3.OperationalError as e:
            return e

    def get_all(self, where=''):
        if where == '':
            where = '1 > 0'

        try:
            query = self.__conn.execute(f"SELECT * FROM routes WHERE {where}")
            data = query.fetchall()
            return data
        except sqlite3.OperationalError as e:
            return e

    def insert(self):
        try:
            self.__conn.execute(
                f"INSERT INTO routes (origen, destino, duracion, valor) VALUES ('{self.origen}', '{self.destino}', {self.duracion}, {self.valor});"
            )
            self.__conn.commit()
            return True
        except Exception as e:
            print(f"Error al insertar: {e}")
            return False

    def update(self):
        try:
            self.__conn.execute(
                f"UPDATE routes SET origen = '{self.origen}', destino = '{self.destino}', duracion = {self.duracion}, valor = {self.valor} WHERE id = {self.id}"
            )
            self.__conn.commit()
            return True
        except Exception as e:
            print(f"Error al actualizar: {e}")
            return False


    def delete(self):
        try:
            self.__conn.execute(f"DELETE FROM routes WHERE id = {self.id}")
            self.__conn.commit()
            return True
        except Exception as e:
            print(f"Error al eliminar: {e}")
            return False
