
edad = int(input("Proporciona tu edad: "))
Etapa = None
if edad >= 0 and edad < 10:
    Etapa = "La infancia es increíble..."
elif edad >= 10 and edad < 20:
    Etapa = "Muchos cambios y mucho estudio..."
elif edad >= 20 and edad <= 30:
    Etapa = "Amor y comienza el trabajo..."
else:
    Etapa = "Etapa de vida no reconocida."
print(f"{Etapa}")