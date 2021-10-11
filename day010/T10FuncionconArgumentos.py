# Crear una función para sumar los valores recibidos de tipo numérico,
# utilizando argumentos variables *args como parámetro de la función y
# regresar como resultado la suma de todos los valores pasados como argumentos.

def sumarValores(*numericos):

    resultado = 0
    for valores in numericos:
        resultado += valores
    return resultado

print(sumarValores(2,4,5))


