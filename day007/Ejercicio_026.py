# 4)Hacer un programa para que dado un número igual o superior a 2 determine si es perfecto o no.
# 	Un número es perfecto cuando es igual a la suma de sus divisores positivos menores que él.
# 	Por ejemplo el 6, que es igual a la suma de 1+2+3.

print('###')
# acumulador = 0
num = int(input('Ingrese número: '))
contador = 0
for perfecto in range(num):
    if (perfecto % 2) == 0:
        contador = contador + num / 2
