# 3)Hacer un programa para ingresar por teclado cuatro números, sumar los dos primeros y los dos segundos; si la
# suma de los dos primeros es mayor a la suma de los dos segundos emitir un cartel aclaratorio, caso contrario no
# emitir nada.
print('#####')
num_1 = int(input('Ingrese primer número: '))
num_2 = int(input('Ingrese segundo número: '))
num_3 = int(input('Ingrese tercero número: '))
num_4 = int(input('Ingrese cuarto número: '))
sum_1 = num_1 + num_2
sum_2 = num_3 + num_4
if sum_1 > sum_2:
    print(f'La suma de los dos primeros es mayor: {sum_1} > {sum_2}')
else:
    print(f'La suma de los dos primeros es menor: {sum_1} < {sum_2}')
