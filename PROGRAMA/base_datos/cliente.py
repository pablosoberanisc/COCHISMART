from base_datos.conexion import obtener_conexion

def registrar_clientes(nombre, telefono, direccion):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    try:
        cursor.execute("""
            INSERT INTO cliente (nombre, telefono, direccion)
            VALUES (:1, :2, :3)
        """, (nombre, telefono, direccion))
        conexion.commit()
        print("Cliente registrado ")
    except Exception as e:
        print("Error al registrar cliente ", e)
    finally:
        cursor.close()
        conexion.close()

def eliminar_clientes(id_cliente):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    try:
        cursor.execute("DELETE FROM cliente WHERE id_cliente = :1", (id_cliente,))
        if cursor.rowcount == 0:
            print("ID no encontrada:c ")
        else:
            conexion.commit()
            print("Cliente eliminado ")
    except Exception as e:
        print("Error al eliminar cliente ", e)
    finally:
        cursor.close()
        conexion.close()

def ver_clientes():
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    try:
        cursor.execute("SELECT id_cliente, nombre, telefono, direccion, fecha_registro FROM cliente")
        clientes = cursor.fetchall()
        for c in clientes:
            print(f"ID: {c[0]}, Nombre: {c[1]}, Teléfono: {c[2]}, Dirección: {c[3]}, Fecha registro: {c[4]}")
    except Exception as e:
        print("Algo salio mal ", e)
    finally:
        cursor.close()
        conexion.close()
    