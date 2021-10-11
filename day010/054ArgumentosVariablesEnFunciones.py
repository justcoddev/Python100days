def listarNombres(*nombres): #Se convierte en tupla *args
    for nombre in nombres:
        print(nombre)

listarNombres('Juan', 'Karla', 'Maria', 'Ernesto')
listarNombres('Laura', 'Carlos')