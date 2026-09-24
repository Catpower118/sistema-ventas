from components.logica import Logica    
import flet as ft         

class Vista:
    def __init__(self, page: ft.Page):
        self.page = page
        self.Logica = Logica 
        self.text_entrada = ft.Text("\n1. Registar venta.\n2. Ver ventas.\n3. Producto mas vendido.")   
        
    