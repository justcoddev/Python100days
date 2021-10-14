# 1)Hacer un programa para ingresar por teclado dos números; si son iguales emitir por pantalla un cartel
# aclaratorio que diga “SON IGUALES”, caso contrario no emitir nada.
print('¿Los números son Iguales?')
num_1 = int(input('Ingrese primer número: '))
num_2 = int(input('Ingrese segundo número: '))

if num_1 == num_2:
    print(f'Los números {num_1} y {num_2} son iguales')
else:
    print('Los números no son iguales')