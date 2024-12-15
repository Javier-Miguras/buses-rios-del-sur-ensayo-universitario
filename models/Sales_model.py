import sqlite3

class SalesModel:
    def __init__(self):
        self.__conn = sqlite3.connect("trabajo.db")
        self.__id = None
        self.__fecha = None
        self.__id_vendedor = None
        self.__subtotal = None
        self.__total = None
        self.__iva = None
        self.__code = None

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def fecha(self):
        return self.__fecha

    @fecha.setter
    def fecha(self, value):
        self.__fecha = value

    @property
    def id_vendedor(self):
        return self.__id_vendedor

    @id_vendedor.setter
    def id_vendedor(self, value):
        self.__id_vendedor = value

    @property
    def subtotal(self):
        return self.__subtotal

    @subtotal.setter
    def subtotal(self, value):
        self.__subtotal = value

    @property
    def iva(self):
        return self.__iva

    @iva.setter
    def iva(self, value):
        self.__iva = value

    @property
    def total(self):
        return self.__total

    @total.setter
    def total(self, value):
        self.__total = value

    @property
    def code(self):
        return self.__code

    @code.setter
    def code(self, value):
        self.__code = value

    def get(self):
        query = self.__conn.execute(f"SELECT * FROM sales WHERE id = {self.id}")
        data = query.fetchone()
        return data

    def get_where(self, where=''):
        if where == '':
            where = '1 > 0'
        try:
            query = self.__conn.execute(f"SELECT * FROM sales WHERE {where}")
            data = query.fetchone()
            return data
        except sqlite3.OperationalError as e:
            return e

    def get_all(self, where=''):
        if where == '':
            where = '1 > 0'

        try:
            query = self.__conn.execute(f"SELECT * FROM sales WHERE {where}")
            data = query.fetchall()
            return data
        except sqlite3.OperationalError as e:
            return e

    def insert(self):
        try:
            self.__conn.execute(
                f"INSERT INTO sales (fecha, id_vendedor, sub_total, iva, total, code) VALUES ('{self.fecha}', {self.id_vendedor}, {self.subtotal}, {self.iva}, {self.total}, '{self.code}');"
            )
            self.__conn.commit()
            return True
        except Exception as e:
            print(f"Error al insertar: {e}")
            return False

    def update(self):
        try:
            self.__conn.execute(
                f"UPDATE sales SET nombre = '{self.nombre}', rut = '{self.rut}' WHERE id = {self.id}"
            )
            self.__conn.commit()
            return True
        except Exception as e:
            print(f"Error al actualizar: {e}")
            return False

    def delete(self):
        try:
            self.__conn.execute(f"DELETE FROM sales WHERE id = {self.id}")
            self.__conn.commit()
            return True
        except Exception as e:
            print(f"Error al eliminar: {e}")
            return False
