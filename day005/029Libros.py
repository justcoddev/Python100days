from datetime import time

print("Proporcione los siguietes datos del libro: ")
nombre = input("Escriba nombre del libro: ")
id = int(input("Escriba el id del libro: "))
precio = float(input("escriba el valor del libro: "))
tipoEnvio = input("indica tipo de envi gratuito(True/false): ")

if tipoEnvio == "True":
    tipoEnvio = True
elif tipoEnvio == 'False':
    tipoEnvio =False
else:
    tipoEnvio = "Valor incorrecto, ecriba True o False"

print(f'''
Nombre: {nombre}
Id: {id}
precio: {precio}
tipo de envio: {tipoEnvio}
''')