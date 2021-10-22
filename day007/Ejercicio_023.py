# 1)	Hacer un programa para ingresar la edad y la altura de 50 personas. Luego se pide determinar e informar:
# 	a) La edad promedio de las 50 personas.
# 	b) La edad promedio de las personas con altura entre 1,60 mts. y 1,80 mts. inclusive.
# 	c) Cantidad de personas con altura mayor a 1,70 mts.
print('####')
acumulador = 0
acumulador2 = 0
contador = 0
contador2 = 0
for i in range(4): # cambiar a 50
    edad = int(input('Escriba la edad '+str(i+1)+': '))
    altura = float(input('Escriba la altura (en metros): '))
    acumulador += edad
    if 1.60 <= altura <= 1.80:
        acumulador2 += edad
        contador2 += 1
    if altura > 1.70:
        contador += 1
promedio = acumulador/4
promedio2 = acumulador2/contador2
print(f'La edad promedio de las 50 personas es: {promedio}')
print(f'La edad promedio de las personas con altura entre 1,60 mts. y 1,80 mts es: {acumulador2}')
print(f'La cantidad de personas con altura mayor a 1,70 mts es: {contador}')
