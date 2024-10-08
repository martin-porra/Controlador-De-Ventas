import pandas as pd 

class Venta:
    __producto = str
    __cantidad = int
    __total = float

    def __init__(self, producto: str, cantidad: int, cobro: float):
        self.__producto = producto  # Nombre del producto
        self.__cantidad = cantidad  # Cantidad de productos
        self.__total = cobro  # Monto cobrado por la venta

    def get_producto(self):
        return self.__producto

    def get_cantidad(self):
        return self.__cantidad

    def get_total(self):
        return self.__total
    

    def __str__(self):
        return f'Producto: {self.__producto}, Cantidad: {self.__cantidad}, Cobro: {self.__cobro}'