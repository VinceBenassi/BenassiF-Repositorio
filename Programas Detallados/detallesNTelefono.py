import phonenumbers as pn
from phonenumbers import carrier, geocoder, timezone as tz

N_Telefono = input("Ingrese un numero de teléfono con el código del país: ")
N_Telefono = pn.parse(N_Telefono)

# Obtener zona horaria del numero de telefono
print(tz.time_zones_for_number(N_Telefono))

# Obtener el operador del número de teléfono
print(carrier.name_for_number(N_Telefono, "es"))

# Obtener información del país
print(geocoder.description_for_number(N_Telefono, "es"))

# Validación del número de teléfono
print("Número de telefono válido...", pn.is_valid_number(N_Telefono))

# Comprobación de la posibilidad del número
print("Comprobando la posibilidad del número...", pn.is_possible_number(N_Telefono))