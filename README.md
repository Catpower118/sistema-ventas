# Sistema de registro de ventas 
Este es un pequeno proyecto desarrollado en Python, Flet y MySQL que registra las ventas del dia y permite visualizar todas en una tabla general a su vez que permite ver los productos que mas se vendieron,
representandolos en una grafica y tabla para mejor visualizacion. Este proyecto esta pensado para pequenos comercios como tiendas de abarrote, ferreterias, etc.. que no buscan un programa complejo si no lo basico 

## Caracteristicas
- Interfaz grafica y moderna
- Registro de ventas y validacion
- Tabla intuitiva y facil de entender
- Arquitectura de capaz 
- Gestion de registro y movimientos con logging

## Requisitos
- Python 3.10+
- MySQL 8.0+
- [Flet](https://flet.dev/)
- mysql-connector-python
- logging
- traceback
- matplotlib

## Instalacion
```bash
git https://github.com/Catpower118/sistema-ventas
cd sistema_ventas
pip install -r requirements.txt
```
## Configuracion MySQL
```sql
CREATE DATABASE sistema_ventas;

CREATE TABLE productos(
id INT AUTO_INCREMENT PRIMARY KEY,
nombre VARCHAR(50) NOT NULL,
cantidad INT NOT NULL,
precio DECIMAL(10, 2) NOT NULL,
fecha DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
)
```

## Ejecucion
```bash
python main.py
```

## Licencia

[MIT license](LICENSE)
