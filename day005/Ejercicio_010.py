# 2)	Hacer un programa para ingresar por teclado dos números y luego calcular y emitir:
#
# - la suma: si el primero es mayor que el segundo.
# - la diferencia: si el primero es menor que el segundo (restarle al segundo el primero)
# - el producto: si ambos son iguales.
# En cualquiera de los casos, el programa calculará y emitirá solo uno de los tres valores.
# Se sugiere resolverlo de dos maneras:
# a) Emitiendo el resultado solamente.
# b) Emitiendo el resultado junto con un cartel aclaratorio, por ejemplo: “La suma es: 10” ó “El producto es 21”.
print('#####')
num_1 = int(input('Ingrese primer número: '))
num_2 = int(input('Ingrese segundo número: '))

if num_1 > num_2:
    suma = num_1 + num_2
    print(f'La suma es: {suma}')
elif num_1 < num_2:
    resta = num_2 - num_1
    print(f'La diferencia es: {resta}')
elif num_1 == num_2:
    multi = num_1 * num_2
    print(f'El producto es: {multi}')

