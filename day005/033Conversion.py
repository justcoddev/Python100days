numero = int(input("Escriba un valor entre 1 y 3: "))
numeroTexto = ""
if numero == 1:
    numeroTexto = "número Uno"
elif numero == 2:
    numeroTexto = "número Dos"
elif numero == 3:
    numeroTexto = "número Tres"
else:
    numeroTexto = "Valor fuera de rango"

print(f"Número proporcionado: {numero} - {numeroTexto}")