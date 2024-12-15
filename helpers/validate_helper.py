import sqlite3
import time
import sys

def validarOpcion(opcion, ini, fin):
    try:
        if int(opcion) >= ini and int(opcion) <= fin:
            return True
        else:
            return False
    except:
        return False
    
def validarId(tabla, id):

    conn = sqlite3.connect("trabajo.db")

    try:
        id = int(id)
        query = f"SELECT * FROM {tabla} WHERE id = {id}"
        result = conn.execute(query)
        
        data = result.fetchone()

        if not data:
            return False
        else:
            return True
    except:
        return False
    
def cerrarApp():
    print("¡Gracias por usar el Sistema! Saliendo...")
    time.sleep(3)
    sys.exit()