# 2)	Un vendedor recibe un sueldo a partir de un importe básico más una comisión de 15% sobre las ventas que haya
# efectuado. Hacer un programa para ingresar por teclado el nombre del vendedor, el sueldo básico y el importe de las
# 3 ventas que efectuó el vendedor y luego calcular e informar el nombre del vendedor y el sueldo total. Atención: El
# importe de cada una de las 3 ventas se ingresa por separado.

name = input('Ingrese nombre del vendedor: ')
sueldoBasico = float(input('Ingrese sueldo básico: '))
venta1 = float(input('Ingrese primera venta:'))
venta2 = float(input('Ingrese segundaa venta:'))
venta3 = float(input('Ingrese tercera venta:'))
comision = (venta1 + venta2 + venta3) * 0.15

sueldoTotal = venta1 + venta2 + venta3 + comision + sueldoBasico

print(f'El vendedor {name} recibe un sueldo total de ${sueldoTotal} ')
