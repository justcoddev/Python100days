# Crear una función para multiplicar los valores recibidos de tipo numérico,
# utilizando argumentos variables *args como parámetro de la función y
# regresar como resultado la multiplicación de todos los valores pasados como argumentos.

def sumarValores(*numericos):

    resultado = 1
    for valores in numericos:
        resultado *= valores
    return resultado

print(sumarValores(2,4,5))

# def multipNumeros(*args):
#     print(f"Los numeros a multiplicar son: {args}")
#     multiplicacion = 1
#     for numero in args:
#         multiplicacion *= numero
#     print(f"La Multiplicación es: {multiplicacion}")
#
# multipNumeros(11, 2, 32, 45, 5, 16, 7, 8, 8)