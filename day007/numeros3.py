numero = int(input("Escriba el rango a iterar: "))
print("Divisible para 3")
for i in range(numero):
    if i % 3 == 0:
        print(f" {i}")
else:
    print("fin de iteración")
# numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for numero in numeros:
#     if numero % 3 == 0:
#         print(numero)