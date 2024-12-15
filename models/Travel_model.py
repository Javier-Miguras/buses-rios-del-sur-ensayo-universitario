import sqlite3

class TravelModel:
    def __init__(self):
        self.__conn = sqlite3.connect("trabajo.db")
        self.__id = None
        self.__id_ruta = None
        self.__id_bus = None
        self.__id_estado = None
        self.__hora_salida = None
        self.__hora_llegada = None
        self.__id_chofer = None

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def id_ruta(self):
        return self.__id_ruta

    @id_ruta.setter
    def id_ruta(self, value):
        self.__id_ruta = value

    @property
    def id_bus(self):
        return self.__id_bus

    @id_bus.setter
    def id_bus(self, value):
        self.__id_bus = value

    @property
    def id_estado(self):
        return self.__id_estado

    @id_estado.setter
    def id_estado(self, value):
        self.__id_estado = value

    @property
    def hora_llegada(self):
        return self.__hora_llegada

    @hora_llegada.setter
    def hora_llegada(self, value):
        self.__hora_llegada = value

    @property
    def hora_salida(self):
        return self.__hora_salida

    @hora_salida.setter
    def hora_salida(self, value):
        self.__hora_salida = value

    @property
    def id_chofer(self):
        return self.__id_chofer

    @id_chofer.setter
    def id_chofer(self, value):
        self.__id_chofer = value

    def get(self):
        query = self.__conn.execute(f"SELECT * FROM travels WHERE id = {self.id}")
        data = query.fetchone()
        return data

    def get_where(self, where=''):
        if where == '':
            where = '1 > 0'
        try:
            query = self.__conn.execute(f"SELECT * FROM travels WHERE {where}")
            data = query.fetchone()
            return data
        except sqlite3.OperationalError as e:
            return e

    def get_all(self, where=''):
        if where == '':
            where = '1 > 0'

        try:
            query = self.__conn.execute(f"SELECT * FROM travels WHERE {where}")
            data = query.fetchall()
            return data
        except sqlite3.OperationalError as e:
            return e

    def insert(self):
        try:
            self.__conn.execute(
                f"INSERT INTO travels (nombre, rut) VALUES ('{self.nombre}', '{self.rut}');"
            )
            self.__conn.commit()
            return True
        except Exception as e:
            print(f"Error al insertar: {e}")
            return False

    def update(self):
        try:
            self.__conn.execute(
                f"UPDATE travels SET nombre = '{self.nombre}', rut = '{self.rut}' WHERE id = {self.id}"
            )
            self.__conn.commit()
            return True
        except Exception as e:
            print(f"Error al actualizar: {e}")
            return False

    def delete(self):
        try:
            self.__conn.execute(f"DELETE FROM travels WHERE id = {self.id}")
            self.__conn.commit()
            return True
        except Exception as e:
            print(f"Error al eliminar: {e}")
            return False
