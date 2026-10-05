import matplotlib.pyplot as plt

class Grafica:
    def grafica_top_productos(self, top):
        productos = [p[0] for p in top]
        totales = [p[1] for p in top]
        plt.bar(productos, totales)
        plt.title("Productos más vendidos")
        plt.xlabel("Producto")
        plt.ylabel("Cantidad")
        plt.show()