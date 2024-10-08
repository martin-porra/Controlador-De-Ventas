import pandas as pd
import csv
from venta import Venta

class creadorVenta:
    __listaventa= None

    def __init__(self):
        self.__listaventa = []

    def agregar(self,producto,cantidad,total):
        with open('venta.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([producto, cantidad, total])