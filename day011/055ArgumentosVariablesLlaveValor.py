def listarTerminos(**terminos): #kwargs
    for llave, valor in terminos.items():
        print(f'{llave}: {valor}')

listarTerminos(IDE= 'Integrated Developement Environment', PK = 'Primary key')
listarTerminos(DBMS='Database Management System')
