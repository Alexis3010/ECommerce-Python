from func import *
from produc import *

i=0
cantidad_comprada=[]
tickets= 0
final_dia= 0
compra=True
recibido=0
ciudad= ''
ticket_promedio= 0

print()
print('BIENVENIDO A SU ECOMMERCE DE CONFIANZA')
print('RECUERDA QUE SUPERANDO LOS $250 EN PRODUCTOS TE DESCONTAMOS EL 35%!')
print()
print()

while compra==True:
    ciudad=ciudades(ciudad)
    habilitar (productos,cantidad_comprada)
    flag=True
        
    while flag==True:
        muestra(productos, precios, stocks)
        print()
        i=verificar(productos)
        print()
        comprar(productos, precios, stocks, i, cantidad_comprada)
        print()
        flag=seguir()

    recibido=pago(productos, cantidad_comprada, stocks, precios, envio, ciudad, recibido)
    tickets=ticket(tickets)
    compra=otra_compra(cantidad_comprada)

ticket_promedio= promedio(recibido, tickets)

print()
print (f'Ticket promedio: {ticket_promedio}')
print()
print('·····················································')
print('Recuerda recomendarnos con tus amigos')
print('¡Que tengas un buen día! :)')
print('·····················································')
input('¿Qué te parecio esta aplicacion? Deja un comentario: ')
