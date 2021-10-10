#diccionarios
#dict (key, value)
diccionario = {
    'IDE':'Integrates Development Environment',
    'OOP': 'Object Oriented Programming',
    'DBMS':'Database Management System'
}
print(diccionario)
#largo
print(len(diccionario))
#acceder a un elemento(key)
print(diccionario['IDE'])
#otra forma de recuperar un elemento
print(diccionario.get('OOP'))
#modificar elementos
diccionario['IDE'] = 'integrated development enviroment'
print(diccionario)
#recorrer los elementos
for termino in diccionario:
    print(termino)
#recorrer los elementos y su valor
for termino, valor in diccionario.items():
    print(termino, valor)
#recuperar solo llaves
for termino in diccionario.keys():
    print(termino)
#recuperar los valores
for valor in diccionario.values():
    print(valor)
#Existencia de algún elemento
print('IDE' in diccionario)
#agregar un elemento
diccionario['PK'] = 'Primary key'
print(diccionario)
#remover un elemento
diccionario.pop('DBMS')
print(diccionario)
#limpiar
diccionario.clear()
print(diccionario)
#eliminar diccionario
del diccionario
print(diccionario)

