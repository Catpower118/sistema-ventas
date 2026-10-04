import mysql.connector

class Conexion:
    def __init__(self):
        self.conn = None

    def connection(self, host, user, password, database):
        try:
            self.conn = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database
            )
            return self.conn, "Conexion exitosa"
        except mysql.connector.Error as err:
            self.conn = None
            return None, f"Error de conexion: {err}"