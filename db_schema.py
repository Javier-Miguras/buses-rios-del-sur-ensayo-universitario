import sqlite3

conn = sqlite3.connect("trabajo.db")

conn.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre VARCHAR NOT NULL,
        rut VARCHAR NOT NULL,
	    username VARCHAR NULL DEFAULT NULL,
	    email VARCHAR NULL DEFAULT NULL,
	    password VARCHAR NULL DEFAULT NULL,
        profile_id INTEGER NULL DEFAULT NULL
    );
""")

conn.execute("""
    CREATE TABLE profiles (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        profile VARCHAR NOT NULL
    );
""")

conn.execute("""
    CREATE TABLE IF NOT EXISTS ctas_corrientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        numero_cuenta VARCHAR NOT NULL,
        usuario_id INTEGER NOT NULL,
        saldo DECIMAL(10,2)
    );
""")

conn.execute("""
    CREATE TABLE IF NOT EXISTS cuenta_movimientos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cuenta_id INTEGER NOT NULL,
        tipo_movimiento_id INTEGER NOT NULL,
        saldo_previo DECIMAL(10,2),
        monto_movimiento DECIMAL(10,2),
        saldo_final DECIMAL(10,2),
        fecha_movimiento DATETIME DEFAULT CURRENT_TIMESTAMP,
        terceros INTEGER DEFAULT 0
    );
""")

conn.execute("""
    CREATE TABLE IF NOT EXISTS tipo_movimientos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tipo_movimiento VARCHAR NOT NULL,
        abono INTEGER DEFAULT 0
    );
""")

conn.execute("""
    INSERT INTO profiles (profile) VALUES
        ('admin'),
        ('vendedor'),
        ('chofer'),
        ('auxiliar');
""")

conn.execute("""
    INSERT INTO tipo_movimientos (tipo_movimiento, abono) VALUES
        ('transferencia bancaria', 0),
        ('giro', 0),
        ('cargos por mantención', 0),
        ('depósito en efectivo', 1),
        ('pago con tarjeta de débito', 0),
        ('pago de línea de crédito', 1),
        ('intereses por línea de crédito', 0),
        ('préstamo recibido', 1),
        ('pago de servicio', 0),
        ('devolución de dinero', 1),
        ('transferencia entre cuentas propias', 0),
        ('cobros por sobregiro', 0),
        ('intereses ganados', 1);
""")

conn.commit()

