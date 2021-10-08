#Definit una tupla (la tupla es un tipo inmutable)
frutas = ('Naranja', 'Platano', 'Guayaba') #siemrpe poner coma al final aunque sea solo un elemento
print(frutas)
#saber el largo
print(len(frutas))
#acceder a un elemento
print(frutas[0])
#navegacion inversa
print(frutas[-1])
#acceder a un rango
print(frutas[0:1]) #sin incluir el último índice
#recorrer tupla
for fruta in frutas:
    print(fruta, end = ' ')
#cambiar valor a tupla
# frutas[0] = 'Pera' #no funciona porque no se puede modificar
#Conversion de tupla a lista y de manera inversa (no es buena práctica)
frutasLista = list(frutas)
frutasLista[0] = 'Pera'
frutas =tuple(frutasLista)
print('\n', frutas)
#eliminar tupla
del frutas
print(frutas)