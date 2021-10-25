# 10)	Una compañía de electricidad necesita calcular anualmente el consumo que ha registrado cada uno de sus
# usuarios y el monto pagado por cada uno de ellos. Para ello, tiene un lote de registros por cada uno de los
# usuarios con los siguientes datos:
# - Zona (1 a 10)
# - Número de cliente (4 números no correlativos)
# - Lectura del medidor para el mes anterior (kilovatios)
# - Lectura del medidor para el mes actual (kilovatios)
#
# El lote se encuentra agrupado por zona (no ordenado) y finaliza con un registro con zona igual a cero.
# Se pide generar un listado con el siguiente formato:
# Zona: XX
# Cantidad de Usuarios de la zona: XXX
# Total Facturado en la zona: XXX
#
# Zona: XX
# Cantidad de Usuarios de la zona: XXX
# Total Facturado en la zona: XXX
#
# El precio es escalonado según la siguiente escala:
#
# $ 0,10 por kilovatio por los primeros 100 kilovatios de consumo.
# $ 0,12 por kilovatio por el consumo de 101 a 200 kilovatios.
# $ 0,15 por kilovatio por el consumo de 201 kilovatios en adelante.
#
# Alguien que consume 250 kilovatios, debe pagar $ 0,10 x 100 + $ 0,12 x 100 + $ 0,15 x 50.
