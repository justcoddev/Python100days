# En un torneo de fútbol participan 20 equipos. Cada equipo realiza 19 partidos, uno con cada rival.
# Hacer un programa para ingresar por cada equipo un conjunto de 19 registros con los siguientes datos:
# Número del equipo (1 a 20)
# 		- Nombre del equipo (10 caracteres)
# 		- Código del resultado del partido jugado  (1: perdido, 2: empatado, 3: ganado)
#
# Los registros se ingresarán agrupados (no necesariamente ordenados)  por número de equipo.
# Se pide determinar e informar:
#
# a) Para cada equipo su número y total de partidos perdidos, empatados y ganados.
# b) El nombre del equipo que ganó más partidos. Si hay varios con la misma cantidad de partidos ganados,
# entonces informar el primero que se haya detectado con esa cantidad.
numero = int(input('Número del equipo(1 a 20): '))
nombre = input('Nombre del equipo: ')
codigo = int(input('Código del equipo:( 1: perdido, 2: empatado, 3: ganado: '))
