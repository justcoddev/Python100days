# 9) Hacer un programa para ingresar por teclado la nota obtenida por un alumno en una determinada
# materia y luego emitir el cartel aclaratorio que corresponda, de acuerdo a las siguientes condiciones:
# - “Sobresaliente”, si la nota fue 10.
# - “Distinguido”, si la nota fue 9 ó 8.
# - “Bueno”, si la nota fue 7 ó 6.
# - “Aprobado”, si la nota fue 5 ó 4.
# - “Insuficiente”, si la nota fue 3, 2 ó 1.
# - “Ausente”, si la nota fue 0.
#
# El programa de emitir UNO SOLO de los carteles anteriores.
print('#####')
num_1 = int(input('Ingrese primera nota: '))
if num_1 == 10:
    print('Sobresaliente')
elif num_1 == 9 or num_1 == 8:
    print('Distinguido')
elif num_1 == 7 or num_1 == 6:
    print('Bueno')
elif num_1 == 5 or num_1 == 4:
    print('Aprobado')
elif num_1 == 3 or num_1 == 2 or num_1 == 1:
    print('Insuficiente')
elif num_1 == 0:
    print('Ausente')
else:
    print('Error')
