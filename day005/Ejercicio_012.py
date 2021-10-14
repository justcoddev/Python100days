# 4)	Un negocio de perfumería efectúa descuentos en sus ventas según el importe de éstas, con la siguiente escala:
#
# - Si el importe es menor a $100 corresponde un descuento del 5%
# - Si el importe es de entre $100 (inclusive) y hasta $500 (inclusive) corresponde un
#               descuento del 10%
# - Si el importe es mayor a $500 corresponde un descuento del 15%
# El dueño le solicitó a Ud., futuro programador, un programa donde se deba ingresar el
# importe original a pagar por el cliente y que luego se calcule e informe por pantalla el precio final
# con el descuento que corresponda ya aplicado.
print('')
importeOriginal = float(input('Ingrese el importe: '))
print('Informe de Perfumeria')
descuento = None
if importeOriginal < 100:
    descuento = importeOriginal - (importeOriginal * 0.05)
    print(f'Precio final: {descuento} --- Descuento del 5%')
elif 100 <= importeOriginal <= 500:
    descuento = importeOriginal - (importeOriginal * 0.10)
    print(f'Precio final: {descuento} --- Descuento del 10%')
elif importeOriginal > 500:
    descuento = importeOriginal - (importeOriginal * 0.15)
    print(f'Precio final: {descuento} --- Descuento del 15%')
else:
    print('Respuesta erronea')
