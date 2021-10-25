# 11)	Un banco posee un gran número de sucursales distribuidas en diversas zonas. Tiene un lote de registros con los
# siguiente datos:
#
# - Código de zona (1 a 10)
# - Código de sucursal (1 a 35)
# - Nombre del cliente (20 caracteres)
# - Saldo del cliente
# El lote se ingresa agrupado por zona y dentro de zona por sucursal. El fin se indica con un registro con código de
# zona igual a cero.
# Se desea obtener un listado con los saldos de los clientes totalizados por sucursal, por zona y el total general,
# con el siguiente formato:
# Sucursal xx:        Saldo acumulado de todos los clientes: xxxxxxxxxx
# Sucursal xx:        Saldo acumulado de todos los clientes: xxxxxxxxxx
#
# Total Zona xx:    xxxxxxxx
#
# Sucursal xx:        Saldo acumulado de todos los clientes: xxxxxxxxxx
# Sucursal xx:        Saldo acumulado de todos los clientes: xxxxxxxxxx
#
# 					Total Zona xx:    xxxxxxxx
#
# Total General:     xxxxxxxx

# Nota: Se recomienda resolver el ejercicio de dos maneras diferentes. La primera
# suponiendo que los códigos de sucursal no se repiten en distintas zonas. La segunda suponiendo que sí se pueden
# repetir, es decir que por ejemplo podría haber dos sucursales con código 25, una en la zona 1 y otra en la zona 4.
# ¿En que cambia la solución esta aclaración?
