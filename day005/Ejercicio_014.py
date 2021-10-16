# 6)Hacer un programa para ingresar por teclado tres números y luego determinar e informar el máximo de ellos.
print('#####')
num_1 = int(input('Ingrese primer número: '))
num_2 = int(input('Ingrese segundo número: '))
num_3 = int(input('Ingrese tercero número: '))
if num_1 > num_2 and num_1 > num_3:
    print(f'El número máximo es el primero: {num_1}')
elif num_2 > num_1 and num_2 > num_3:
    print(f'El número máximo es el segundo: {num_2}')
else:
    print(f'El número máximo es el tercero: {num_3}')
