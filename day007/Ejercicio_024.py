# 2)Hacer un programa para ingresar por teclado una lista de 10 números, luego determinar e  informar cuantos son
# positivos, cuantos son negativos, y cuantos iguales a cero.
print('####')
numeros = []
positivo = 0
negativo = 0
cero = 0
for i in range(10):
    numero = int(input('Ingrese número '+str(i+1)+': '))
    numeros.append(numero)
    if numero > 0:
        positivo += 1
    elif numero < 0:
        negativo += 1
    elif numero == 0:
        cero += 1
print(f'Lista de números: {numeros}')
print(f'Positivos: {positivo}')
print(f'Negativos: {negativo}')
print(f'Cero: {cero}')
