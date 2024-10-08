
import pandas as pd

df = pd.read_csv('venta.csv',header=None)
# Poner la lista nombres como columna
nombres = ['Producto', 'Cantidad', 'Precio']#
df.columns = nombres 
df.to_csv('venta.csv', index=False)
print(df.head())