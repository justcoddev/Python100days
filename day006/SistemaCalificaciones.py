nota = int(input("Proporcione un valor entre 0 y 10: "))
letra = None
if nota >= 9 and nota <= 10:
    letra = "A"
elif nota >= 8 and nota < 9:
    letra = "B"
elif nota >= 7 and nota < 8:
    letra = "C"
elif nota >= 6 and nota < 7:
    letra = "D"
elif nota >= 0 and nota < 6:
    letra = "F"
else:
    letra = "Valor desconocido"
print(f"Su calificación es: \"{letra}\"")