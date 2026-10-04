from components.logica import Logica    
import flet as ft         

class Vista:
    def __init__(self, page: ft.Page):
        self.page = page
        self.Logica = Logica() 
        self.contenedor_principal = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text("Bienvenido", color="blue", size=50, weight="bold")
                    ]
                ),
            expand=True,
            padding=10,
            bgcolor="white",
            border_radius=10,
            alignment=ft.Alignment.CENTER
        )
        self.entrada_sesion = ft.TextField(label="Usuario", border_color="blue", cursor_color="blue", color="blue")
        self.localhost_sesion = ft.TextField(label="Host", border_color="blue", cursor_color="blue", color="blue")
        self.contrasena_sesion = ft.TextField(label="contrasena", border_color="blue",
                                              cursor_color="blue", color="blue", password=True, can_reveal_password=True)
        self.database_sesion = ft.TextField(label="DataBase", border_color="blue", cursor_color="blue", color="blue")
        
        # ENTRADAS PRODUCTOS
        self.producto_entrada = ft.TextField(label="Producto", border_color="blue", cursor_color="blue")
        self.cantidad_entrada = ft.TextField(label="Cantidad", border_color="blue", cursor_color="blue")
        self.precio_entrada = ft.TextField(label="Precio", border_color="blue", cursor_color="blue")
        
    # SIDEBAR
    def sidebar(self):
        return ft.Container(
            width=200,
            bgcolor="blue",
            padding=10,
            content=ft.Column(
                controls=[
                    ft.Text("Registro", size=20, color="white", weight="bold"),
                    ft.Divider(color="white"),
                    ft.TextButton("Iniciar sesion", icon=ft.Icons.DASHBOARD,
                                  style=ft.ButtonStyle(color="white"), on_click=self.vista_login),
                    ft.TextButton("Registrar ventas", icon=ft.Icons.RECEIPT_LONG, 
                                  style=ft.ButtonStyle(color="white"), on_click=self.vista_registrar_venta),
                    ft.TextButton("Ver ventas", icon=ft.Icons.PEOPLE,
                                  style=ft.ButtonStyle(color="white"), on_click=self.vista_ver_ventas),
                    ft.TextButton("Productos mas vendidos", icon=ft.Icons.INVENTORY,
                                  style=ft.ButtonStyle(color="white"), on_click=self.vista_productos_top)
                ],
                spacing=10
            ),
            border_radius=10
        )
    # VISTA DE SESION, REGISTRO DE VENTAS, VER VENTAS Y PRODUCTOS TOP
    def vista_login(self, e):
        self.contenedor_principal.content = ft.Column(
            controls=[
                ft.Text("Iniciar sesion", color="blue", size=30, weight="bold"),
                self.localhost_sesion,
                self.entrada_sesion,
                self.contrasena_sesion,
                self.database_sesion,
                ft.Button("Iniciar", bgcolor="blue", color="white", on_click=self.sesion_frontend)
            ]
        )
        self.page.update()

    def vista_registrar_venta(self, e):
        self.contenedor_principal.content = ft.Column(
            controls=[
                ft.Text("Registrar venta", size=30, weight="bold", color="blue"),
                self.producto_entrada,
                self.cantidad_entrada,
                self.precio_entrada,
                ft.Button("Guardar venta", bgcolor="blue", color="white", on_click=self.guardar_venta_frontend)
            ]
        )
        self.page.update()

    def vista_ver_ventas(self, e):
        self.contenedor_principal.content = ft.Column(
            controls=[
                ft.Text("Ventas registradas", size=30, weight="bold"),
                self.tabla()
            ]
        )
        self.page.update()

    def vista_productos_top(self, e):
        self.contenedor_principal.content = ft.Column(
            controls=[
                ft.Text("Productos más vendidos", size=30, weight="bold"),
                self.ranking()
            ]
        )
        self.page.update()
        
    
    # TABLA DE VENTAS Y RANKING DE PRODUCTOS
    def tabla(self):
        tabla = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("ID", color="green")),
                ft.DataColumn(ft.Text("Producto", color="green")),
                ft.DataColumn(ft.Text("Precio", color="green")),
                ft.DataColumn(ft.Text("Fecha", color="green"))
            ],
            rows=[]
        )
        return ft.Container(
            content=ft.Column(
                controls=[tabla],
                scroll="auto",
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.START
            ),
            width=700,
            height=500,
            padding=10,
            margin=10,
            bgcolor="black",
            border_radius=10    
        )
    
    def ranking(self):
        table = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("ID", color="green")),
                ft.DataColumn(ft.Text("Producto", color="green")),
                ft.DataColumn(ft.Text("Cantidad", color="green"))
            ],
            rows=[]
        ) 
        contenedor = ft.Container(
            content=ft.Column(
                controls=[table],
                scroll="auto",
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.START
            ),
            width=400,
            height=300,
            padding=10,
            margin=10,
            bgcolor="black",
            border_radius=10    
        )
        ranking_contenedor = ft.Container(
            content=ft.Text("Ranking de productos más vendidos", size=20, weight="bold", color="blue"),
            width=400,
            height=250,
            padding=10,
            margin=10,
            bgcolor="#AC9F9F",
            border_radius=10
        )
        return ft.Column(
            controls=ft.Row(
                controls=[ranking_contenedor, contenedor],
                spacing=10,
                alignment=ft.MainAxisAlignment.CENTER
            ),
            spacing=10,
            alignment=ft.MainAxisAlignment.CENTER
        )
        
    # MENSAJES DE ALERTA
    def mensaje_exito(self, mensaje):
        alerta = ft.AlertDialog(
            title=ft.Text("Éxito", color="green"),
            content=ft.Text(mensaje, color="green"),
            actions=[
                ft.TextButton("Aceptar", on_click=lambda e: self.page.pop_dialog())
            ]
        )
        self.page.show_dialog(alerta)
        
    def mensaje_error(self, mensaje):
        alerta = ft.AlertDialog(
            title=ft.Text("Error", color="red"),
            content=ft.Text(mensaje , color="red"),
            actions=[
                ft.TextButton("Aceptar", on_click=lambda e: self.page.pop_dialog())
            ]
        )
        self.page.show_dialog(alerta)
        
    # METODOS PARA AGREGAR LOS PRODUCTOS Y TABLAS
    def guardar_venta_frontend(self, e):
        try:
            producto = self.producto_entrada.value
            cantidad = self.cantidad_entrada.value
            precio = self.precio_entrada.value
        
            exito, mensaje = self.Logica.guardar_venta(producto, cantidad, precio)
        
            if exito:
                self.mensaje_exito(mensaje)
            else:
                self.mensaje_error(mensaje)
        except Exception as e:
            self.mensaje_error(f"Ha ocurrido un error: {e}")
        finally:
            self.producto_entrada.value = ""
            self.cantidad_entrada.value = ""
            self.precio_entrada.value = ""
            self.page.update()
            
    def sesion_frontend(self, e):
        try:
            usuario = self.entrada_sesion.value
            puerto = self.localhost_sesion.value
            contrasena = self.contrasena_sesion.value
            database = self.database_sesion.value
            
            exito, mensaje = self.Logica.sesion(puerto, usuario, contrasena, database)
            
            if exito:
                self.mensaje_exito(mensaje)
            else:
                self.mensaje_error(mensaje)
        except Exception as e:
            self.mensaje_error(f"Ha ocurrido un error: {e}")
        finally:
            self.entrada_sesion.value = ""
            self.localhost_sesion.value = ""
            self.contrasena_sesion.value = ""
            self.database_sesion.value = ""
            self.page.update()
            

