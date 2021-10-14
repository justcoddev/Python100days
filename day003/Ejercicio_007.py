# 7)Un comercio vende tres marcas de alfajores distintas: Sabroso, Goloso y Apetitoso. El dueño le pide a Ud.,
# futuro programador, un programa para que se pueda ingresar por teclado la cantidad de alfajores vendidos durante el
# día para cada una de las tres marcas en el orden anteriormente indicado (es decir se ingresan 3 datos distintos) y
# luego se calcule e informe el porcentaje de ventas para cada una de ellas.
# Por ejemplo: se ingresa 100, 25 y 75 como cantidades vendidas entonces el programa
# calculará e informará Sabroso: 50%, Goloso 12,50% y Apetitoso 37,50%.
print('Comercio de Alfajores')
print('Ingrese cantidad de alfajores vendidos')
aSabroso = int(input('Alfajores Sabrosos: '))
aGoloso = int(input('Alfajores Goloso: '))
aApetitoso = int(input('Alfajores Apetitoso: '))
tVendidos = aSabroso + aGoloso + aApetitoso
vSabroso = aSabroso/tVendidos * 100
vGoloso = aGoloso/tVendidos * 100
vApetitoso = aApetitoso/tVendidos * 100
print(f'Alfajores vendidos en Porcentajes')
print(f'Sabroso: {vSabroso}%\nGoloso: {vGoloso}%\nApetitoso: {vApetitoso}%')
