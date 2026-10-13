from config.conexion import Conexion
from mysql.connector import Error
from utils.generar_log import Logging
import traceback

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
        except Error as e:
            Logging.add_to_log("error", str(e))
            Logging.add_to_log("error", traceback.format_exc())
            return False, f"Error al guardar la venta: {e}"

    def obtener_ventas(self):
        if self.conexion.conn is None:
            return [], "Error: No hay conexion a la base de datos."
        try:
            cursor = self.conexion.conn.cursor()
            cursor.execute("SELECT id, producto, precio, fecha FROM ventas ORDER BY fecha DESC")
            datos = cursor.fetchall()
            cursor.close()
            return datos, None
        except Error as e:
            Logging.add_to_log("error", str(e))
            Logging.add_to_log("error", traceback.format_exc())
            return [], f"Error al obtener ventas: {e}"

    def obtener_top_productos(self):
        if self.conexion.conn is None:
            return [], "Error: No hay conexion a la base de datos."
        try:
            cursor = self.conexion.conn.cursor()
            cursor.execute("SELECT producto, SUM(cantidad) AS total FROM ventas GROUP BY producto ORDER BY total DESC LIMIT 10")
            datos = cursor.fetchall()
            cursor.close()
            return datos, None
        except Error as e:
            Logging.add_to_log("error", str(e))
            Logging.add_to_log("error", traceback.format_exc())
            return [], f"Error al obtener ranking: {e}"
        
    def traer_registro(self):
        if self.conexion.conn is None:
            return False, "Error: No hay conexion a la base de datos. Llene los campos de sesion."
        try:
            cursor = self.conexion.conn.cursor()
            sql = "SELECT * FROM ventas"
            cursor.execute(sql)
            resultado = cursor.fetchall()
            cursor.close()
            return True, resultado
        except Error as e:
            Logging.add_to_log("error", str(e))
            Logging.add_to_log("error", traceback.format_exc())
            return False, f"Error al traer el registro: {e}"
        