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