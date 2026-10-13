from view.vista import Vista
import flet as ft          

def main(page: ft.Page):
    page.title = "Sistema de ventas"
    page.bgcolor = "black"
    page.window.icon = "venta_fondo.ico"
    
    mostrar = Vista(page)
    
    page.add(
        ft.Row(
            controls=[
                mostrar.sidebar(),
                mostrar.contenedor_principal
            ],
            expand=True
        )
    )
    
    
if __name__ == "__main__":
    ft.run(main, assets_dir="assets")