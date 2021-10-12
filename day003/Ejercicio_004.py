# 4)En un hospital existen tres áreas y el presupuesto anual del hospital se distribuye
# conforme a la siguiente tabla:
#     Área		Porcentaje del presupuesto
# Ginecología			40%
# Traumatología			30%
# Pediatría			    30%
# Hacer un programa para ingresar el monto del presupuesto anual del hospital y luego
# calcular e informar el importe que obtendrá cada una de las áreas.

print('Presupuesto Anual del Hospital')
presupuesto = float(input('Ingrese el presupuesto anual: '))
ginecologia = presupuesto * 0.4
traumatologia = presupuesto * 0.3
pediatria = presupuesto * 0.3

print('Porcentaje correspondiente a cada área ')
print(f'Ginecología: {ginecologia}% \nTraumatología: {traumatologia}% \nPediatría: {pediatria}%')