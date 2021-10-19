# 14)	Una fórmula permite determinar si una persona tiene un peso normal, bajo o excedido.
# La fórmula es la siguiente:
#
# X=Estatura (en cm.)-Peso (en Kg.)
# 	       100
# El valor de X es un coeficiente que se relaciona con la edad de la persona de la siguiente manera:
#                    Hasta 20 años	       Más de 20 hasta 30  	    Más de 30 hasta 40	        Más de 40
# Peso normal	    X entre 0,90 y 1,10	    X entre 0,85 y 1,15 	X entre 0,80 y 1,10	        X entre 0,75 y 1,10
# Bajo peso     	X más de 1,10	            X más de 1,15	    X más de 1,10	          X más de 1,10
# Excedido	        X menos de 0,90             X menos de 0,85 	X menos de 0,80	            X menos de 0,75
# Confeccionar un programa para que a partir del ingreso de los datos: estatura (en cm),
# peso (en Kg) y edad (en años), informe si la persona tiene un peso normal, bajo o excedido.
# Por ejemplo si se ingresa Estatura: 180 cm, Peso: 70 kg, Edad: 28, se calculará:
# 180 – 70=110 / 100 = 1,1. Como la edad está entre 20 y 30, X = 1,1 es Peso Normal.
print('####')
edad = int(input('Ingrese la edad: '))
estatura = int(input('Ingrese estatura: '))
peso = int(input('Ingrese peso: '))
equis = (estatura - peso) / 100

if edad <= 20:
    if 0.90 < equis < 1.10:

        print('ff')
else:
    print('gg')
