hora = int(input("¿A qué hora llegó el cliente? (0-23): "))

if 6 <= hora <= 11:
    print("Turno: mañana")
elif 12 <= hora <= 17:
    print("Turno: tarde")
elif 18 <= hora <= 22:
    print("Turno: noche")
else:
    print("Fuera de horario")