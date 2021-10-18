# 12)	Una empresa de electricidad cobra el servicio a sus clientes de acuerdo a la siguiente escala:
# $ 0,10 por kilovatio por los primeros 100 kilovatios de consumo.
# $ 0,12 por kilovatio por el consumo de 101 a 200 kilovatios.
# $ 0,15 por kilovatio por el consumo de 201 kilovatios en adelante.
# Hacer un programa para que dado el consumo en kilovatios de un determinado cliente,
# el programa calcule e informe el total a pagar por el mismo.
# Ejemplo 1: Si se ingresa un consumo de 55 kilovatios, entonces el programa calculará:
# $ 0,10 x 55= $ 5,50
# Ejemplo 2: Si se ingresa un consumo de 125 kilovatios, entonces el programa calculará:
# $ 0,10 x 100 + $ 0,12 x 25=$ 13
# Ejemplo 3: Si se ingresa un consumo de 250 kilovatios, entonces el programa calculará:
# $ 0,10 x 100 + $ 0,12 x 100 + $ 0,15 x 50 = $ 29,50.
print('#####')
name = input('Nombre del cliente: ')
kilovatios = int(input('Ingrese Kilovatios consumidos: '))
if kilovatios <= 100:
    pkilovatios = kilovatios * 0.10
    print(f'Su consumo ha sido calculado:\n$0.10 * {kilovatios} kilovatios = {pkilovatios} kilovatios')
elif 101 < kilovatios < 200:
    # skilovatiosdiv = kilovatios / 100
    # pkilovatios = int(skilovatiosdiv * 0.10)
    pkilovatios = 0.10 * 100
    skilovatiosmod = kilovatios % 100
    skilovatios = skilovatiosmod * 0.12
    total = pkilovatios + skilovatios
    print(f'Su consumo ha sido calculado:\n$0.10 * 100 kilovatios + $0.12 * {skilovatiosmod} = {total} kilovatios')
elif kilovatios > 201:
    # 200 kilovatios = 22
    pkilovatios = 0.10 * 100
    skilovatios2 = 0.12 * 100
    skilovatiosmod = kilovatios % 200
    skilovatios = skilovatiosmod * 0.15
    total = pkilovatios + skilovatios2 + skilovatios
    print(f'Su consumo ha sido calculado:\n$0.10 * 100 kilovatios + $0.12 * 100 + $0.15 * {skilovatiosmod} '
          f'= {total}kilovatios')
