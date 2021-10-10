#set = el orden no está presente
planetas = {'Marte', 'Júpiter', 'Venus'}
print(planetas)
#largo
print(len(planetas))
#revisar si un elemento está presente
print('Marte' in planetas)
print('Martes' in planetas)
#Agregar un elemento
planetas.add('Tierra')
print(planetas)
#no se peuden dupliar eleme3ntos
planetas.add('Tierra')
print(planetas)
#eliminar elementos posiblemente arrojando un error
planetas.remove('Tierra')
print(planetas)
#eliminar elemento sin arrojar error
planetas.discard('Jupiter')
print(planetas)
#limpiar set
planetas.clear()
print(planetas)
#eliminar el set
del planetas
print(planetas)
