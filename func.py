#TICKET, VALIDACION Y MÁS
envio= 50
#ciudad
def ciudades(ciudad):
    while True:
        ciudad=input('POR FAVOR INGRESE SU CIUDAD:   ')
        if ciudad.isnumeric():
            print()
            print('Usted ha ingresado un numero..')
        else:
            return ciudad



#HABILITAR OBJETOS A LA COMPRA
def habilitar(productos, cantidad_comprada):
    for producto in productos:
        cantidad_comprada.append(0)


#MUESTRA DE OBJETOS

def muestra(productos, precios, stocks):
    print('·····················································')
    print()
    for i in range(len(productos)):
        producto = productos[i]
        precio = precios[i]
        stock = stocks[i]
        print(f'Producto: {producto} - Precio: ${precio} - Stock: {stock}')
        print()
    print('·····················································')

#CONTROLAR STOCK

def comprar(productos, precios, stocks, i, cantidad_comprada):
    print(f"El PRECIO del producto '{productos[i]}' es de ${precios[i]}.")
    print()
    print(f"El STOCK del producto '{productos[i]}' es de {stocks[i]} unidades.")
    while True:
        if stocks[i]==0:
            print(f"No hay suficientes unidades de '{productos[i]}' en stocks.")
            break
        cantidad = input('¿Cuántas unidades desea comprar? ')
        if cantidad.isnumeric():
            cantidad = int(cantidad)
            if cantidad <= stocks[i] and cantidad!=0:
                print(f"Usted ha comprado {cantidad} unidades de '{productos[i]}'.")
                stocks[i] -= cantidad 
                cantidad_comprada[i] += cantidad 
                break
            elif cantidad==0:
                    print('No se puede comprar 0 unidades.')
            else:
                print(f"No hay suficientes unidades de '{productos[i]}' en stocks.")
        else:
            print('Por favor ingrese un número.')

#SEGUIR COMPRANDO 

def seguir():
    while True:
        seguir = input('¿Desea seguir comprando? ').strip().lower()
        if seguir!='no' and seguir!='si':
            print('..............................')
            print('Por favor ingrese SI o NO.')
        if seguir=='no':
            return False
        elif seguir=='si':
            return True
 
#CIERRE DE CAJA, TICKET
def pago (productos, cantidad_comprada, stocks, precios, envio, ciudad, recibido):
    gastado=0
    gasto_total= 0
    gastado_descuento= 0 
    descuento=35
    compras_realizadas = False
    descuento_aplicado= 0
    finalizar= True

    print()
    print('Ticket:')
    for i in range(len(productos)):
        cantidad = cantidad_comprada[i]
        if cantidad > 0:
            producto = productos[i]
            precio = precios[i]  
            gasto_producto = cantidad * precio
            gastado += gasto_producto
            print()
            print(f'Producto: {producto} - Cantidad comprada: {cantidad}')
            print(f'Precio a pagar: ${precio*cantidad}')
            print(f'')
    gasto_total= gastado+envio
    compras_realizadas = True
    if gastado>250:
        gastado_descuento = ( descuento * gasto_total )/ 100  
        descuento_aplicado = gasto_total - gastado_descuento         
    if compras_realizadas:
        print()
        print(f'Usted ha gastado un total de ${gastado} en productos.') 
        print(f'Con un envio a: {ciudad}')
        print(f'El costo del envio es de: ${envio}')
        print(f'Pago total: ${gasto_total}')
        print()
        if gastado_descuento>0:
            print(f'SE HA APLICADO UN DESCUENTO DE {descuento}%')
            print(f'PAGO FINAL: ${descuento_aplicado}')
            print()
            print()
            recibido+=descuento_aplicado
            return recibido
        elif gastado_descuento==0:
            recibido+=gasto_total
            return recibido

        
#generador de ticket
def ticket(tickets):
    tickets+=1
    return tickets
    

#seguir comprando
def otra_compra(cantidad_comprada):
    cantidad_comprada.clear()
    while True: 
        comprar=input('¿Desea realizar otra compra?').strip().lower()
        if comprar!='si' and comprar!='no':
            print('Por favor ingrese SI o NO.')
            print()
        if comprar=='si':
            return True
        if comprar=='no':
            return False

        
#ticket promedio
def promedio(recibido, tickets):
    recibido= recibido / tickets
    return recibido
