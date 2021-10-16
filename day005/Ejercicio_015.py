# 7)Una empresa calcula sus sueldos multiplicando al valor de la hora y la cantidad de horas que trabajó cada
# empleado. Además si el empleado trabajó más de 100 horas lo premian con $100.- y si trabajó más de 200 horas el
# premio es de $250 La empresa le solicitó a Ud., futuro programador, un programa para poder ingresar por teclado
# el valor de la hora y la cantidad de horas trabajadas por un empleado y luego determinar e informar
# por pantalla el sueldo que corresponda abonarle.
horas = int(input('Ingrese horas trabajadas: '))
valor = int(input('Ingrese valor de hora: '))
total = valor * horas

if 100 < horas <= 200:
    total = total + 100
    print(f'El sueldo total es ${total}')
elif horas > 200:
    total = total + 250
    print(f'El sueldo total es ${total}')
else:
    print(f'El sueldo total es ${total}')
