# 1)	Hacer un programa para ingresar la edad y la altura de 50 personas. Luego se pide determinar e informar:
# 	a) La edad promedio de las 50 personas.
# 	b) La edad promedio de las personas con altura entre 1,60 mts. y 1,80 mts. inclusive.
# 	c) Cantidad de personas con altura mayor a 1,70 mts.
print('####')
acumulador = 0
acumulador2 = 0
contador = 0
for i in range(4):
    edad = int(input('Escriba la edad: '))
    altura = int(input('Escriba la altura: '))
    acumulador += edad
    if 1.60 <= altura <= 1.80:
        acumulador2 += edad
        if altura > 170:
            contador += 1
print(f'La edad promedio de las 50 personas es: {acumulador}')
print(f'La edad promedio de las personas con altura entre 1,60 mts. y 1,80 mts es: {acumulador2}')
print(f'La cantidad de personas con altura mayor a 1,70 mts es: ')
