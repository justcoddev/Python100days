# 11)	Un negocio vende distintos artículos identificados por un código entre 1 y 4. Los precios
# de los artículos y las condiciones de venta son las siguientes:
#
# - Artículos con código 1: $ 10 por unidad
# - Artículos con código 2: $ 7 pesos por unidad y $ 65 la caja con 10 unidades.
# - Artículos con código 3: $ 3 pesos por unidad, si la compra es por más de 10 unidades se
#   aplica un 10% de descuento sobre el total de la compra.
# - Artículos con código 4: $ 1 peso por unidad
# Hacer un programa para ingresar por teclado: el código del artículo, la cantidad vendida y luego
# se pide calcular e informar el importe a pagar por el cliente.
# Observaciones:
# - El programa solo sirve para ingresar un solo código de artículo y una sola cantidad en cada ejecución.
# - Si el artículo vendido es el 2 calcular las cajas y los sueltos por separado.
# Se sugiere consultar el ejercicio similar de los alfajores en el TP 1.
# - Si el artículo vendido es el 3 el descuento del 10% no es acumulable, es decir que
# corresponde un 10% tanto si la cantidad es de 11 unidades como si es de 100 unidades.
print('#####')
codigo = int(input('Ingrese Código del artículo: '))
cantidad = int(input('Ingrese cantidad que desea comprar: '))
if codigo == 1:
    total = cantidad * 10
    print(f'El valor a pagar es de ${total}')
elif codigo == 2:
    caja = int(cantidad / 10)
    vCaja = caja * 65
    unidad = cantidad % 10
    vUnidad = unidad * 7
    total = vCaja + vUnidad
    print(f'El vcalor a pagar es ${vCaja} la caja y ${vUnidad} la unidad siendo un total de ${total}')
elif codigo == 3:
    if cantidad > 10:
        unidad = cantidad * 3
        descuento = unidad-(unidad * 0.10)
        print(f'El valor a pagar con un descuento del 10% es de ${descuento}')
    else:
        unidad = cantidad * 3
        print(f'El valor a pagar es ${unidad}')
elif codigo == 4:
    unidad = cantidad * 1
    print(f'El valor a pagar es ${unidad}')
else:
    print('Error al ingresar código..')
