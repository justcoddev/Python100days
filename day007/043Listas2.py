#Definir una Lista de tipo str
nombres = ["Juan","Karla","Ricardo", "María"]
#imprimir la lista de nombre
print(nombres)
#accerder a lso elementos de una lista
print(nombres[0])
print(nombres[1])
#acceder a los elementos de manera inversa
print(nombres[-1])
print(nombres[-2])
#Imprimir rango
print(nombres[0:2]) #sin incluir indice 2
#Ir del indice de la lsita al indice (sin incluirlo)
print(nombres[:3])
#Desde indice indicado hasta el final de lista
print(nombres[1:])
#Cambiar valor indice
nombres[3] = "Ivone"
print(nombres)
#iterar lsita
for nombre in nombres:
    print(nombre)
else:
    print("no existen más nombres en la lista")