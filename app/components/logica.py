from database.queries import DataBase        
from config.conexion import Conexion
import re    



class Logica:
    def __init__(self):
        self.conexion = Conexion()
        self.db = DataBase(self.conexion)
        
        
    def guardar_venta(self, producto, cantidad, precio):
        if not producto or not cantidad or not precio:
            return False, "Error: Todos los campos son obligatorios."
        if precio.count(".") > 1:
            return False, "Error: El precio no debe contener mas de un (.) decimal."
        if not re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúÑñ0-9 ]+", producto):
            return False, "Error: El nombre solo debe contener letras, numeros y espacios."
        try:
            cantidad_int = int(cantidad)
            precio_float = float(precio)
        except ValueError:
            return False, "Error: La cantidad y el precio deben ser numeros validos."
        if cantidad_int <= 0:
            return False, "Error: La cantidad debe ser un numero positivo."
        if precio_float <= 0:
            return False, "Error: El precio debe ser un numero positivo."
        
        return self.db.insertar_venta(producto, cantidad_int, precio_float) 
    
    def obtener_ventas(self):
        return self.db.obtener_ventas()

    def obtener_top_productos(self):
        return self.db.obtener_top_productos()

    def sesion(self, host, usuario, contrasena, database):
        if not host or not usuario or not contrasena or not database:
            return False, "Error: Todos los campos son obligatorios."
        
        exito, mensaje = self.conexion.connection(host, usuario, contrasena, database)
        if exito:
            return True, mensaje
        else:
            return False, mensaje