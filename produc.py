#PRODUCTOS : listas PRECIO PRODUCTO Y STOCKS

productos=['tv','pc','netbook']
precios=[ 100 , 200 , 300 ]
stocks=[ 5, 10, 8]

ind=0

#BUSCAR PRODUCTO
def verificar(productos):
    while True:
        buscar = input('¿Qué desea comprar? ').lower().strip()
        
        if buscar in productos:
            ind = productos.index(buscar)
            print(f"El producto '{buscar}' fue encontrado en la lista.")
            return ind
        else:
            print('Producto no encontrado en la lista. Intente nuevamente.')

