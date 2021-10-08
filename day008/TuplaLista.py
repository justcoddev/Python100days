
tuplaNumeros = (13, 1, 8, 3, 2, 5, 8)
print(f'Tupla: {tuplaNumeros}')
print("Números menores que 5 ")
listaNumeros = []
for numero in tuplaNumeros:
    if numero < 5:
        print(numero, end = ' ')
        listaNumeros.append(numero)


else:
    print("\nFin ciclo for")
print(f'Números menores que 5 colocados en una lista: {listaNumeros}')