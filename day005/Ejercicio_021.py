# 13)	Una empresa de venta de boletos de micros tiene distintas tarifas según el destino, servicio (común o
# diferencial) y compañía elegida por el pasajero. La siguiente tabla indica los precios a pagar por el servicio
# común por pasajero:
# Compañía	Destino 1	Destino 2	Destino 3
#    1	    $ 20.-  	$ 15.-	    $ 30.-
#   2	    $ 22.-	    $ 16,50	    $ 33.-
#   3	    $ 24.-  	$ 18.-  	$ 36.-
# El servicio diferencial cuesta un 20% más.
# Además, si el pasajero compra 5 o más pasajes juntos se ofrece un descuento del 15% .
# El dueño de la empresa le solicitó a Ud., futuro programador,
# un programa para ingresar los siguientes datos por cada venta:
#
# -	Número de Destino (1 a 3)
# -	Compañía (1, 2, 3)
# -	Cantidad de pasajes solicitados por el pasajero
# -	Servicio (1=  común, 2= diferencial )
#
# El programa sólo permite ingresar una venta por vez y calcula y emite el importe neto a pagar.
print('#######')
destino = int(input('Número d destino(1, 2, 3): '))
company = int(input('Ingrese compañía(1, 2, 3): '))
servicio = int(input('Servicio: \n1 = Común\n2 = Diferencial\n: '))
pasajes = int(input('Ingrese cantidad de pasajes: '))
if destino == 1:
    if company == 1:
        if servicio == 1:
            valorComun = pasajes * 20
            if pasajes >= 5:
                descuentoComun = valorComun - (valorComun * 0.15)
                print(f'El valo a pagar por el servicio común es de: ${descuentoComun}')
            else:
                print(f'El valo a pagar por el servicio común es de: ${valorComun}')
        elif servicio == 2:
            valorDiferencial = pasajes * 24
            if pasajes >= 5:
                descuentoDiferencial = valorDiferencial - (valorDiferencial * 0.15)
                print(f'El valo a pagar por el servicio común es de: ${descuentoDiferencial}')
            else:
                print(f'El valo a pagar por el servicio común es de: ${valorDiferencial}')
    elif company == 2:
        if servicio == 1:
            valorComun = pasajes * 22
            if pasajes >= 5:
                descuentoComun = valorComun - (valorComun * 0.15)
                print(f'El valo a pagar por el servicio común es de: ${descuentoComun}')
            else:
                print(f'El valo a pagar por el servicio común es de: ${valorComun}')
        elif servicio == 2:
            valorDiferencial = pasajes * 26.40
            if pasajes >= 5:
                descuentoDiferencial = valorDiferencial - (valorDiferencial * 0.15)
                print(f'El valo a pagar por el servicio común es de: ${descuentoDiferencial}')
            else:
                print(f'El valo a pagar por el servicio común es de: ${valorDiferencial}')
    elif company == 3:
        if servicio == 1:
            valorComun = pasajes * 24
            if pasajes >= 5:
                descuentoComun = valorComun - (valorComun * 0.15)
                print(f'El valo a pagar por el servicio común es de: ${descuentoComun}')
            else:
                print(f'El valo a pagar por el servicio común es de: ${valorComun}')
        elif servicio == 2:
            valorDiferencial = pasajes * 28.8
            if pasajes >= 5:
                descuentoDiferencial = valorDiferencial - (valorDiferencial * 0.15)
                print(f'El valo a pagar por el servicio común es de: ${descuentoDiferencial}')
            else:
                print(f'El valo a pagar por el servicio común es de: ${valorDiferencial}')
elif destino == 2:
    if company == 1:
        if servicio == 1:
            valorComun = pasajes * 15
            if pasajes >= 5:
                descuentoComun = valorComun - (valorComun * 0.15)
                print(f'El valo a pagar por el servicio común es de: ${descuentoComun}')
            else:
                print(f'El valo a pagar por el servicio común es de: ${valorComun}')
        elif servicio == 2:
            valorDiferencial = pasajes * 18
            if pasajes >= 5:
                descuentoDiferencial = valorDiferencial - (valorDiferencial * 0.15)
                print(f'El valo a pagar por el servicio común es de: ${descuentoDiferencial}')
            else:
                print(f'El valo a pagar por el servicio común es de: ${valorDiferencial}')
    elif company == 2:
        if servicio == 1:
            valorComun = pasajes * 16.50
            if pasajes >= 5:
                descuentoComun = valorComun - (valorComun * 0.15)
                print(f'El valo a pagar por el servicio común es de: ${descuentoComun}')
            else:
                print(f'El valo a pagar por el servicio común es de: ${valorComun}')
        elif servicio == 2:
            valorDiferencial = pasajes * 19.80
            if pasajes >= 5:
                descuentoDiferencial = valorDiferencial - (valorDiferencial * 0.15)
                print(f'El valo a pagar por el servicio común es de: ${descuentoDiferencial}')
            else:
                print(f'El valo a pagar por el servicio común es de: ${valorDiferencial}')
    elif company == 3:
        if servicio == 1:
            valorComun = pasajes * 18
            if pasajes >= 5:
                descuentoComun = valorComun - (valorComun * 0.15)
                print(f'El valo a pagar por el servicio común es de: ${descuentoComun}')
            else:
                print(f'El valo a pagar por el servicio común es de: ${valorComun}')
        elif servicio == 2:
            valorDiferencial = pasajes * 21.60
            if pasajes >= 5:
                descuentoDiferencial = valorDiferencial - (valorDiferencial * 0.15)
                print(f'El valo a pagar por el servicio común es de: ${descuentoDiferencial}')
            else:
                print(f'El valo a pagar por el servicio común es de: ${valorDiferencial}')
elif destino == 3:
    if company == 1:
        if servicio == 1:
            valorComun = pasajes * 30
            if pasajes >= 5:
                descuentoComun = valorComun - (valorComun * 0.15)
                print(f'El valo a pagar por el servicio común es de: ${descuentoComun}')
            else:
                print(f'El valo a pagar por el servicio común es de: ${valorComun}')
        elif servicio == 2:
            valorDiferencial = pasajes * 36
            if pasajes >= 5:
                descuentoDiferencial = valorDiferencial - (valorDiferencial * 0.15)
                print(f'El valo a pagar por el servicio común es de: ${descuentoDiferencial}')
            else:
                print(f'El valo a pagar por el servicio común es de: ${valorDiferencial}')
    elif company == 2:
        if servicio == 1:
            valorComun = pasajes * 33
            if pasajes >= 5:
                descuentoComun = valorComun - (valorComun * 0.15)
                print(f'El valo a pagar por el servicio común es de: ${descuentoComun}')
            else:
                print(f'El valo a pagar por el servicio común es de: ${valorComun}')
        elif servicio == 2:
            valorDiferencial = pasajes * 39.60
            if pasajes >= 5:
                descuentoDiferencial = valorDiferencial - (valorDiferencial * 0.15)
                print(f'El valo a pagar por el servicio común es de: ${descuentoDiferencial}')
            else:
                print(f'El valo a pagar por el servicio común es de: ${valorDiferencial}')
    elif company == 3:
        if servicio == 1:
            valorComun = pasajes * 36
            if pasajes >= 5:
                descuentoComun = valorComun - (valorComun * 0.15)
                print(f'El valo a pagar por el servicio común es de: ${descuentoComun}')
            else:
                print(f'El valo a pagar por el servicio común es de: ${valorComun}')
        elif servicio == 2:
            valorDiferencial = pasajes * 43.20
            if pasajes >= 5:
                descuentoDiferencial = valorDiferencial - (valorDiferencial * 0.15)
                print(f'El valo a pagar por el servicio común es de: ${descuentoDiferencial}')
            else:
                print(f'El valo a pagar por el servicio común es de: ${valorDiferencial}')
    print(f'gg')
