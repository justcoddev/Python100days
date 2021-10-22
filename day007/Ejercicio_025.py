# 3)Hacer un programa para ingresar las 20 notas de los alumnos de un curso, luego informar:
#   a) La cantidad de alumnos aprobados (nota >= 4)
# 	b) La cantidad de alumnos aplazados (nota <= 3)
# 	c) La cantidad de alumnos promocionados (nota >=9)
# Atención: Los alumnos promocionados deben ser contabilizados también como aprobados.

print('###')
apr = 0
apl = 0
pro = 0
for i in range(5):
    nota = int(input('Ingrese nota '+str(i+1)+':'))
    if nota >= 4:
        apr += 1
    elif nota <= 3:
        apl += 1
    elif nota >= 9:
        pro += 1
print(f'Aprobados: {apr}')
print(f'Aplazados: {apl}')
print(f'Promocionados: {pro}')
