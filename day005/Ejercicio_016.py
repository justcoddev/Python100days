# 8)Hacer un programa para ingresar por teclado las cuatro notas de los exámenes parciales obtenidas
# por un alumno en una determinada materia y luego emitir el cartel aclaratorio que corresponda,
# de acuerdo a las siguientes condiciones:
# - “Promociona”, si obtuvo en los cuatro exámenes nota 7 o más.
# - “Rinde examen final”, si obtuvo nota 4 o más en por lo menos tres exámenes.
# - “Recupera Parciales”, si obtuvo nota 4 o más en por lo menos uno de los exámenes.
# - “Recursa la materia”, si no aprobó ningún examen parcial.
#
# El programa de emitir UNO SOLO de los carteles anteriores.
print('#####')
num_1 = int(input('Ingrese primera nota: '))
num_2 = int(input('Ingrese segunda nota: '))
num_3 = int(input('Ingrese tercera nota: '))
num_4 = int(input('Ingrese cuarta nota: '))
if (num_1 >= 7 and num_2 >= 7) and (num_3 >= 7 and num_4 >= 7):
    print(f'PROMOCIONA')
elif (num_1 >= 4 and num_2 >= 4 and num_3 >= 4 and num_4 != 4) or \
        (num_1 >= 4 and num_2 >= 4 and num_3 != 4 and num_4 >= 4) or\
        (num_1 >= 4 and num_2 != 4 and num_3 >= 4 and num_4 >= 4) or \
        (num_1 != 4 and num_2 >= 4 and num_3 >= 4 and num_4 >= 4) or \
        (num_1 >= 4 and num_2 >= 4 and num_3 >= 4 and num_4 >= 4):
    print(f'Rinde examen final')
elif (num_1 >= 4 and num_2 != 4 and num_3 != 4 and num_4 != 4) or \
        (num_1 != 4 and num_2 >= 4 and num_3 != 4 and num_4 != 4) or\
        (num_1 != 4 and num_2 != 4 and num_3 >= 4 and num_4 != 4) or \
        (num_1 != 4 and num_2 != 4 and num_3 != 4 and num_4 >= 4):
    print(f'Recupera Parciales')
else:
    print(f'Recursa la materia')
