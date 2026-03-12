servicios = ["masaje", "facial", "manicure"]

servicio = input("¿Qué servicio deseas? (masaje / facial / manicure): ")

if servicio in servicios:
    print(f"¡Perfecto! Tu servicio de {servicio} ha sido registrado.")
else:
    print("Lo sentimos, ese servicio no está disponible.")