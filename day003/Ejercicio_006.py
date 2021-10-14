# 6) En una materia se obtiene la calificación final para cada alumno a partir de varias notas en diversos
# exámenes y trabajos prácticos. Cada alumno realiza tres parciales, un examen final y un trabajo práctico.
# La nota final se calcula a partir de sumar:
# - 55% del promedio de sus tres exámenes parciales
# - 30% de la calificación del examen final
# - 15% de la calificación del trabajo final
# Hacer un programa para ingresar por teclado el nombre del alumno, la nota de los tres exámenes parciales,
# la nota del examen final y la nota del trabajo final, luego calcular e informar la nota final,
# junto al nombre del alumno.
# Atención: La nota es en todos los casos un número entre 0 y 100.
# Por ejemplo se ingresan como datos: 70, 40 y 100 para los parciales, 70 para el examen final y 70
# para el trabajo final. Ese alumno obtiene como nota final: 38,50 + 21 + 10,50 = 70
print('Calificaciones')
name = int(input('Nombre del estudiante: '))
print('Ingrese la nota de los parciales')
parcial_1 = int(input('Parcial 1: '))
parcial_1 = int(input('Parcial 2: '))
parcial_1 = int(input('Parcial 3: '))
examenFinal = int(input('Examen final: '))
trabajoFinal = int(input('Trabajo Final: '))
