duracion_fase = 3
num_fase = int(input('Ingrese numero de fase: '))
cuota_mensual = 60

tiempo_meses = num_fase * duracion_fase
tiempo_años = tiempo_meses * 1 / 12
dinero_invertido = tiempo_meses * cuota_mensual
print(f'\nTiempo invertido fue: {tiempo_meses} meses')
print(f'Tiempo invertido fue: {tiempo_años} años')
print(f'Dinero invertido fue: ${dinero_invertido}')