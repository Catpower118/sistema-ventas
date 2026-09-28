from components.logica import Logica    
import flet as ft         

class Vista:
    def __init__(self, page: ft.Page):
        self.page = page
        self.Logica = Logica 
        self.contenedor_principal = ft.Container(
            expand=True,
            padding=10,
            bgcolor="blue"
        )
        
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
                    ft.TextButton("Iniciar sesion", style=ft.ButtonStyle(color="white")),
                    ft.TextButton("Registrar venta", style=ft.ButtonStyle(color="white")),
                    ft.TextButton("Ver ventas", style=ft.ButtonStyle(color="white")),
                    ft.TextButton("Productos mas vendidos", style=ft.ButtonStyle(color="white"))
                ],
                spacing=10
            )
        )
    
    # CONTENIDO PRINCIPAL
    def contenido(self):
        return ft.Container(
            expand=True,
            padding=10,
            bgcolor="white",
            content=ft.Column(
                controls=[
                    ft.Text("Bienvenido")
                ]
            )
        )

