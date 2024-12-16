import sqlite3
import pandas as pd
import os # Para usar rutas relativas

class ReportModel:
    def __init__(self):
        self.__conn = sqlite3.connect("trabajo.db")

    def sales_all(self, where=''):
        if where == '':
            where = '1 > 0'

        try:
            query = f"""
                SELECT 
                    t.id as nro_pasaje,
                    s.fecha as fecha_venta,
                    u.nombre as nombre_vendedor,
                    u.rut as rut_vendedor,
                    r.origen as ciudad_origen,
                    r.destino as ciudad_destino,
                    tr.hora_salida,
                    tr.hora_llegada,
                    b.patente as patente_bus,
                    us.nombre as chofer,
                    us.rut as rut_chofer,
                    ts.estado as estado_viaje,
                    s.sub_total,
                    s.iva,
                    s.total,
                    s.code as codigo_venta
                FROM tickets t
                LEFT JOIN sales s ON t.id_venta = s.id
                LEFT JOIN usuarios u ON s.id_vendedor = u.id
                LEFT JOIN travels tr ON t.id_viaje = tr.id
                LEFT JOIN routes r ON tr.id_ruta = r.id
                LEFT JOIN buses b ON tr.id_bus = b.id
                LEFT JOIN travel_status ts ON tr.id_estado = ts.id
                LEFT JOIN usuarios us ON tr.id_chofer = us.id
                WHERE {where}
            """
            # Ejecuta la consulta y carga los datos en un DataFrame
            df = pd.read_sql_query(query, self.__conn)

            # Ruta relativa a la carpeta "exports" dentro del proyecto
            ruta_carpeta = "./reports/"
            nombre_archivo = "reporte_ventas.xlsx"
            ruta_completa = os.path.join(ruta_carpeta, nombre_archivo)

            # Crea la carpeta "exports" si no existe
            if not os.path.exists(ruta_carpeta):
                os.makedirs(ruta_carpeta)

            # Exporta el DataFrame a un archivo Excel
            df.to_excel(ruta_completa, index=False)
        except sqlite3.OperationalError as e:
            return e
