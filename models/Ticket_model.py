import sqlite3

class TicketModel:
    def __init__(self):
        self.__conn = sqlite3.connect("trabajo.db")
        self.__id = None
        self.__id_venta = None
        self.__nombre_pasajero = None
        self.__rut_pasajero = None
        self.__id_viaje = None

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def id_venta(self):
        return self.__id_venta

    @id_venta.setter
    def id_venta(self, value):
        self.__id_venta = value

    @property
    def nombre_pasajero(self):
        return self.__nombre_pasajero

    @nombre_pasajero.setter
    def nombre_pasajero(self, value):
        self.__nombre_pasajero = value

    @property
    def rut_pasajero(self):
        return self.__rut_pasajero

    @rut_pasajero.setter
    def rut_pasajero(self, value):
        self.__rut_pasajero = value

    @property
    def id_viaje(self):
        return self.__id_viaje

    @id_viaje.setter
    def id_viaje(self, value):
        self.__id_viaje = value

    def get(self):
        query = self.__conn.execute(f"SELECT * FROM tickets WHERE id = {self.id}")
        data = query.fetchone()
        return data
    
    def get_complete_ticket(self, where=''):
        if where == '':
            where = '1 > 0'
        try:
            query = self.__conn.execute(f"""
                SELECT
                    s.id as nro_venta,
                    s.code as codigo_venta,
                    t.id as nro_pasaje,
                    s.fecha as fecha_venta,
                    u.nombre as nombre_vendedor,
                    u.rut as rut_vendedor,
                    r.origen as ciudad_origen,
                    r.destino as ciudad_destino,
                    ti.nombre_pasajero,
                    ti.rut_pasajero,
                    tr.hora_salida,
                    tr.hora_llegada,
                    b.patente as patente_bus,
                    us.nombre as chofer,
                    us.rut as rut_chofer,
                    ts.estado as estado_viaje,
                    s.sub_total,
                    s.iva,
                    s.total
                FROM tickets t
                LEFT JOIN sales s ON t.id_venta = s.id
                LEFT JOIN usuarios u ON s.id_vendedor = u.id
                LEFT JOIN travels tr ON t.id_viaje = tr.id
                LEFT JOIN routes r ON tr.id_ruta = r.id
                LEFT JOIN buses b ON tr.id_bus = b.id
                LEFT JOIN travel_status ts ON tr.id_estado = ts.id
                LEFT JOIN usuarios us ON tr.id_chofer = us.id
                LEFT JOIN tickets ti ON s.id = ti.id_venta
                WHERE {where}
            """)
            data = query.fetchone()
            return data
        except sqlite3.OperationalError as e:
            return e

    def get_where(self, where=''):
        if where == '':
            where = '1 > 0'
        try:
            query = self.__conn.execute(f"SELECT * FROM tickets WHERE {where}")
            data = query.fetchone()
            return data
        except sqlite3.OperationalError as e:
            return e

    def get_all(self, where=''):
        if where == '':
            where = '1 > 0'

        try:
            query = self.__conn.execute(f"SELECT * FROM tickets WHERE {where}")
            data = query.fetchall()
            return data
        except sqlite3.OperationalError as e:
            return e

    def insert(self):
        try:
            self.__conn.execute(
                f"INSERT INTO tickets (id_venta, nombre_pasajero, rut_pasajero, id_viaje) VALUES ({self.id_venta}, '{self.nombre_pasajero}', '{self.rut_pasajero}', {self.id_viaje});"
            )
            self.__conn.commit()
            return True
        except Exception as e:
            print(f"Error al insertar: {e}")
            return False

    def update(self):
        try:
            self.__conn.execute(
                f"UPDATE tickets SET nombre = '{self.nombre}', rut = '{self.rut}' WHERE id = {self.id}"
            )
            self.__conn.commit()
            return True
        except Exception as e:
            print(f"Error al actualizar: {e}")
            return False

    def delete(self):
        try:
            self.__conn.execute(f"DELETE FROM tickets WHERE id = {self.id}")
            self.__conn.commit()
            return True
        except Exception as e:
            print(f"Error al eliminar: {e}")
            return False
