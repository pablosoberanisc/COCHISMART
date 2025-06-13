from base_datos.conexion import obtener_conexion

def registrar_producto(nombre_producto, descripcion, precio_unitario, disponible='S'):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    try:
        cursor.execute("""
            INSERT INTO producto (nombre_producto, descripcion, precio_unitario, disponible)
            VALUES (:1, :2, :3, :4)
        """, (nombre_producto, descripcion, precio_unitario, disponible))
        conexion.commit()
        print("Producto registrado ")
    except Exception as e:
        print("Error al registrar producto ", e)
    finally:
        cursor.close()
        conexion.close()

def eliminar_producto(id_producto):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    try:
        cursor.execute("DELETE FROM producto WHERE id_producto = :1", (id_producto,))
        if cursor.rowcount == 0:
            print("ID no encontrada:c ")
        else:
            conexion.commit()
            print("Producto eliminado ")
    except Exception as e:
        print("Error al eliminar cliente ", e)
    finally:
        cursor.close()
        conexion.close()

def ver_productos():
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    try:
        cursor.execute("SELECT id_producto, nombre_producto, descripcion, precio_unitario, disponible FROM producto")
        clientes = cursor.fetchall()
        for c in clientes:
            print(f"ID: {c[0]}, Nombre: {c[1]}, Descripción: {c[2]}, Precio: {c[3]}, Disponibilidad: {c[4]}")
    except Exception as e:
        print("Algo salio mal ", e)
    finally:
        cursor.close()
        conexion.close()