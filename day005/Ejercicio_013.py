# 5)Hacer un programa para ingresar por teclado la longitud de los tres lados de un triángulo,
# luego se pide determinar e informar con un cartel aclaratorio que tipo de triángulo es:
#
# - Equilátero: si los tres lados son iguales
# - Isósceles: si dos de los tres lados son iguales
# - Escaleno: si los tres lados son distintos entre sí
print('Tipo de Triángulo')
lado_1 = int(input('Lado 1 : '))
lado_2 = int(input('Lado 2 : '))
lado_3 = int(input('Lado 3 : '))
if lado_1 == lado_2 == lado_3:
    print(f'Equilátero:Los tres lados son iguales')
elif (lado_1 == lado_2) or (lado_1 == lado_3) or (lado_2 == lado_3):
    print(f'Isósceles:Dos de los tres lados son iguales')
elif lado_1 != lado_2 and lado_2 != lado_3 and lado_2 != lado_3:
    print(f'Escaleno: Los tres lados son distintos entre sí')
else:
    print('Error')
