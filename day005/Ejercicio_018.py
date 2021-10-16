# 10)	Una empresa calcula sus sueldos multiplicando el valor de la hora y la cantidad de horas que trabajó cada
# empleado. Tener en cuenta que se deben deducir $ 150.- en concepto de impuestos, si el sueldo total es igual o
# excede a los $ 4.000. La empresa le solicitó a Ud., futuro programador, un programa para poder ingresar por teclado
# el valor de la hora y la cantidad de horas trabajadas por un empleado y luego determinar e informar por pantalla el
# sueldo que le corresponda abonarle.
horas = int(input('Ingrese horas trabajadas: '))
valor = int(input('Ingrese valor de hora: '))
total = valor * horas


if total >= 4000:
    total = total - 150
    print(f'El sueldo total es ${total}')
else:
    print(f'El sueldo total es ${total}')
