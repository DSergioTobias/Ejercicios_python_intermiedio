categorias = {"bajo compromiso": 0, "compromiso medio": 0, "compromiso alto": 0}

for i in range(1, 6):
    nombre = input(f"\nPersona {i} - Nombre: ")
    dias = int(input("Días asistidos: "))
    minutos = int(input("Minutos promedio por día: "))

    if dias < 3:
        categoria = "bajo compromiso"
    elif dias <= 4:
        categoria = "compromiso medio"
    else:
        categoria = "compromiso alto"

    categorias[categoria] += 1
    print(f"{nombre} → {categoria} ({dias} días, {minutos} min/día)")

print("\n===== Resumen =====")
for categoria, cantidad in categorias.items():
    print(f"{categoria}: {cantidad} persona(s)")