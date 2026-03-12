capacidad = int(input("Capacidad de la sala: "))
ninos, adultos, mayores = 0, 0, 0
total = 0

while True:
    if total >= capacidad:
        break
    if input("\n¿Ingresar persona? (si/no): ") == "no":
        break

    edad = int(input("Edad: "))
    if edad < 12:
        ninos += 1
    elif edad < 60:
        adultos += 1
    else:
        mayores += 1
    total += 1

print(f"\nTotal: {total}")
print(f"Niños: {ninos} | Adultos: {adultos} | Adultos mayores: {mayores}")
print("Sala llena" if total >= capacidad else "Sala no llena")