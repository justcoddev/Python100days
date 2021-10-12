# 3)	Hacer un programa para ingresar por teclado la cantidad de asientos disponibles en un avión y la cantidad de
# pasajes vendidos (es decir la cantidad de asientos ocupados) y luego calcular e informar el porcentaje de ocupación
# del mismo. Por ejemplo si el avión tiene 200 asientos disponibles y se vendieron 80 pasajes, el porcentaje de
# ocupación que se informará será de un 40%. Nota: Los valores 200 y 80 son solamente para ejemplificar,
# no debe hacer un programa para ingresar solamente esos valores, debe ser genérico

print('Informe del porcentaje de asientes ocupados en un avión')
disponibles = int(input('Igrese cantidad de asientos disponibles: '))
vendidos = int(input('Ingrese cantidad de asientos vendidos: '))
porcentajeVendidos = 100 * (vendidos/disponibles)
print(f'La cantidad de asientos vendidos es de {porcentajeVendidos}%')
