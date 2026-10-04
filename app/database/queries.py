from config.conexion import Conexion

class DataBase:
    def __init__(self, conexion):
        self.conexion = conexion

    def insertar_venta(self, producto, cantidad, precio):
        if self.conexion.conn is None:
            return False, "Error: No hay conexion a la base de datos. Llene los campos de sesion."
        try:
            cursor = self.conexion.conn.cursor()
            sql = "INSERT INTO ventas (producto, cantidad, precio) VALUES (%s, %s, %s)"
            values = (producto, cantidad, precio)
            cursor.execute(sql, values)
            self.conexion.conn.commit()
            cursor.close()
            return True, f"Venta: {producto} guardada exitosamente."
        except Exception as e:
            return False, f"Error al guardar la venta: {e}"