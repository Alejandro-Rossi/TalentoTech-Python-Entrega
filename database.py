import sqlite3

DB_NAME = "stock_computacion.db"


def conectar_db():
    return sqlite3.connect(DB_NAME)


def inicializar_db():
    conexion = None
    try:
        conexion = conectar_db()
        cursor = conexion.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS productos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                marca TEXT NOT NULL,
                modelo TEXT NOT NULL,
                tipo TEXT NOT NULL,
                precio REAL NOT NULL
            )
        """)
        conexion.commit()
    except sqlite3.Error as e:
        print(f"❌ Error crítico al inicializar la base de datos: {e}")
    finally:
        if conexion:
            conexion.close()


def insertar_producto(marca, modelo, tipo, precio):
    """Create: Inserta un nuevo registro en la tabla productos."""
    conexion = None
    try:
        conexion = conectar_db()
        cursor = conexion.cursor()
        cursor.execute(
            "INSERT INTO productos (marca, modelo, tipo, precio) VALUES (?, ?, ?, ?)",
            (marca, modelo, tipo, precio),
        )
        conexion.commit()
        return True
    except sqlite3.Error as e:
        if conexion:
            conexion.rollback()
        print(f"❌ Error al guardar en la base de datos: {e}")
        return False
    finally:
        if conexion:
            conexion.close()


def obtener_todos():
    """Read: Devuelve una lista de tuplas con todos los productos."""
    conexion = None
    try:
        conexion = conectar_db()
        cursor = conexion.cursor()
        cursor.execute("SELECT id, marca, modelo, tipo, precio FROM productos")
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"❌ Error al consultar los productos: {e}")
        return []
    finally:
        if conexion:
            conexion.close()


def obtener_por_id(id_producto):
    """Read: Busca un producto exacto por su clave primaria ID."""
    conexion = None
    try:
        conexion = conectar_db()
        cursor = conexion.cursor()
        cursor.execute(
            "SELECT id, marca, modelo, tipo, precio FROM productos WHERE id = ?",
            (id_producto,),
        )
        return cursor.fetchone()
    except sqlite3.Error as e:
        print(f"❌ Error al buscar por ID: {e}")
        return None
    finally:
        if conexion:
            conexion.close()


def buscar_productos(termino):
    """Read: Busca coincidencias parciales por marca o modelo."""
    conexion = None
    try:
        conexion = conectar_db()
        cursor = conexion.cursor()
        patron = f"%{termino}%"
        cursor.execute(
            """
            SELECT id, marca, modelo, tipo, precio
            FROM productos
            WHERE LOWER(marca) LIKE LOWER(?) OR LOWER(modelo) LIKE LOWER(?)
            """,
            (patron, patron),
        )
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"❌ Error al realizar la búsqueda: {e}")
        return []
    finally:
        if conexion:
            conexion.close()


def actualizar_producto(id_producto, marca, modelo, tipo, precio):
    """Update: Actualiza los campos de un producto existente."""
    conexion = None
    try:
        conexion = conectar_db()
        cursor = conexion.cursor()
        cursor.execute(
            """
            UPDATE productos
            SET marca = ?, modelo = ?, tipo = ?, precio = ?
            WHERE id = ?
            """,
            (marca, modelo, tipo, precio, id_producto),
        )
        conexion.commit()
        return cursor.rowcount > 0
    except sqlite3.Error as e:
        if conexion:
            conexion.rollback()
        print(f"❌ Error al actualizar el producto: {e}")
        return False
    finally:
        if conexion:
            conexion.close()


def eliminar_producto(id_producto):
    """Delete: Elimina un producto por su ID."""
    conexion = None
    try:
        conexion = conectar_db()
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM productos WHERE id = ?", (id_producto,))
        conexion.commit()
        return cursor.rowcount > 0
    except sqlite3.Error as e:
        if conexion:
            conexion.rollback()
        print(f"❌ Error al eliminar el producto: {e}")
        return False
    finally:
        if conexion:
            conexion.close()