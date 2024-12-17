import sqlite3

class UsuarioModel:
    def __init__(self):
        self.__conn = sqlite3.connect("trabajo.db")
        self.__id = None
        self.__nombre = None
        self.__rut = None
        self.__username = None
        self.__email = None
        self.__password = None
        self.__profile_id = None

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, value):
        self.__nombre = value

    @property
    def rut(self):
        return self.__rut

    @rut.setter
    def rut(self, value):
        self.__rut = value

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        self.__username = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        self.__password = value

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value

    @property
    def profile_id(self):
        return self.__profile_id

    @profile_id.setter
    def profile_id(self, value):
        self.__profile_id = value

    def get(self):
        query = self.__conn.execute(f"SELECT * FROM usuarios WHERE id = {self.id}")
        data = query.fetchone()
        return data

    def get_where(self, where=''):
        if where == '':
            where = '1 > 0'
        try:
            query = self.__conn.execute(f"SELECT * FROM usuarios WHERE {where}")
            data = query.fetchone()
            return data
        except sqlite3.OperationalError as e:
            return e

    def get_all(self, where=''):
        if where == '':
            where = '1 > 0'

        try:
            query = self.__conn.execute(f"SELECT * FROM usuarios WHERE {where}")
            data = query.fetchall()
            return data
        except sqlite3.OperationalError as e:
            return e

    def insert(self):
        try:
            self.__conn.execute(
                f"INSERT INTO usuarios (nombre, rut, username, email, password, profile_id) VALUES ('{self.nombre}', '{self.rut}', '{self.username}', '{self.email}', '{self.password}', {self.profile_id});"
            )
            self.__conn.commit()
            return True
        except Exception as e:
            print(f"Error al insertar: {e}")
            return False

    def update(self):
        try:
            self.__conn.execute(
                f"UPDATE usuarios SET nombre = '{self.nombre}', rut = '{self.rut}', username = '{self.username}', email = '{self.email}', password = '{self.password}', profile_id = {self.profile_id} WHERE id = {self.id}"
            )
            self.__conn.commit()
            return True
        except Exception as e:
            print(f"Error al actualizar: {e}")
            return False

    def delete(self):
        try:
            self.__conn.execute(f"DELETE FROM usuarios WHERE id = {self.id}")
            self.__conn.commit()
            return True
        except Exception as e:
            print(f"Error al eliminar: {e}")
            return False
