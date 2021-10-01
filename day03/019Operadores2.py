a = int(input("number 1: "))
b = int(input("number 2: "))
sum = a + b
#print('La suma es:', sum)
print(f'La suma es :{sum}') #interpolación
resta = a -  b
print(f'La resta es : {resta}')
mult = a * b
print(f'La multiplicación es : {mult}')
div = a / b
print(f'La división es : {div}') #por defecto es flotantes
div = a//b
print(f'La división(int) es : {div}')
module = a % b
print(f'El residuo es : {module}')
exponente = a ** b
print(f'El resultado del exponente es : {exponente}')