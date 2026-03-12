niveles = {"bajo": 0, "medio": 0, "alto": 0}
total, cantidad, mejor, mejor_nombre = 0, 0, 0, ""

while input("\n¿Registrar estudiante? (si/no): ") == "si":
    nombre = input("Nombre: ")
    promedio = (int(input("Speaking: ")) + int(input("Listening: ")) + int(input("Reading: "))) / 3

    if promedio < 60:
        nivel = "bajo"
    elif promedio < 80:
        nivel = "medio"
    else:
        nivel = "alto"

    niveles[nivel] += 1
    total += promedio
    cantidad += 1

    if promedio > mejor:
        mejor, mejor_nombre = promedio, nombre

    print(f"{nombre} → {promedio:.1f} | {nivel}")

print(f"\nPromedio general: {total/cantidad:.1f}")
print(f"Mejor estudiante: {mejor_nombre} ({mejor:.1f})")
for nivel, n in niveles.items():
    print(f"{nivel}: {n}")