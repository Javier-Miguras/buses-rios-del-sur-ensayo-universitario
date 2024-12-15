import sqlite3

class BusModel:
    def __init__(self):
        self.__conn = sqlite3.connect("trabajo.db")
        self.__id = None
        self.__modelo = None
        self.__patente = None
        self.__capacidad = None
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def modelo(self):
        return self.__modelo

    @modelo.setter
    def modelo(self, value):
        self.__modelo = value

    @property
    def patente(self):
        return self.__patente

    @patente.setter
    def patente(self, value):
        self.__patente = value

    @property
    def capacidad(self):
        return self.__capacidad

    @capacidad.setter
    def capacidad(self, value):
        self.__capacidad = value

    def get(self):
        query = self.__conn.execute(f"SELECT * FROM buses WHERE id = {self.id}")
        data = query.fetchone()
        return data

    def get_where(self, where=''):
        if where == '':
            where = '1 > 0'
        try:
            query = self.__conn.execute(f"SELECT * FROM buses WHERE {where}")
            data = query.fetchone()
            return data
        except sqlite3.OperationalError as e:
            return e

    def get_all(self, where=''):
        if where == '':
            where = '1 > 0'

        try:
            query = self.__conn.execute(f"SELECT * FROM buses WHERE {where}")
            data = query.fetchall()
            return data
        except sqlite3.OperationalError as e:
            return e

    def insert(self):
        try:
            self.__conn.execute(
                f"INSERT INTO buses (modelo, patente, capacidad) VALUES ('{self.modelo}', '{self.patente}', {self.capacidad});"
            )
            self.__conn.commit()
            return True
        except Exception as e:
            print(f"Error al insertar: {e}")
            return False

    def update(self):
        try:
            self.__conn.execute(
                f"UPDATE buses SET modelo = '{self.modelo}', patente = '{self.patente}', capacidad = {self.capacidad} WHERE id = {self.id}"
            )
            self.__conn.commit()
            return True
        except Exception as e:
            print(f"Error al actualizar: {e}")
            return False

    def delete(self):
        try:
            self.__conn.execute(f"DELETE FROM buses WHERE id = {self.id}")
            self.__conn.commit()
            return True
        except Exception as e:
            print(f"Error al eliminar: {e}")
            return False
