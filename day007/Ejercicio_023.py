# 1)	Hacer un programa para ingresar la edad y la altura de 50 personas. Luego se pide determinar e informar:
# 	a) La edad promedio de las 50 personas.
# 	b) La edad promedio de las personas con altura entre 1,60 mts. y 1,80 mts. inclusive.
# 	c) Cantidad de personas con altura mayor a 1,70 mts.
print('####')
# altura = int(input('Escriba la altura: '))
acumulador = 0
for i in range(4):
    edad = int(input('Escriba la edad: '))
    acumulador += edad
print(f'promedio: {acumulador}')
