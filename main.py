from ArchivoVenta import creadorVenta

if __name__ == '__main__':
    archivoventa = creadorVenta()
    producto = 'coca'
    cantidad = 2
    total= 1500
    archivoventa.agregar(producto,cantidad,total)
    
