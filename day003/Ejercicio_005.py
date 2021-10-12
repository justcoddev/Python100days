# 5)Una maestra desea un programa para ingresar por teclado la cantidad de alumnos hombres y alumnas mujeres de un
# curso y obtener el porcentaje respectivo para cada sexo. Por ejemplo, si se ingresa 24 alumnos y 16 alumnas,
# obtendrá como respuesta que en ese curso el 60% son alumnos y el 40% son alumnas.

print('Porcentaje de Varones y Mujeres')
varones = int(input('Ingrese cantidad de alumnos hombres: '))
mujeres = int(input('Ingrese cantidad de alumnas mujeres: '))
curso = varones + mujeres
porcentajeV = varones * 100/curso
porcentajeM = mujeres * 100/curso

print(f'En ese curso el {porcentajeV}% son Alumnos y el {porcentajeM}% son alumnas.')

