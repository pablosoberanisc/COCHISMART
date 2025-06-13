import oracledb

def obtener_conexion():
    return oracledb.connect(
        user="USUARIO_DAVID",
        password="davidsob21",
        dsn="localhost:1521/XE"
    )
