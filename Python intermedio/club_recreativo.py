precios = {"basico": 50000, "premium": 90000, "familiar": 130000}
conteo  = {"basico": 0, "premium": 0, "familiar": 0}
total   = 0

while input("¿Registrar? (si/no): ") == "si":
    edad = int(input("Edad: "))
    plan = input("Plan (basico/premium/familiar): ")
    print("Registro juvenil" if edad < 18 else "Beneficio senior" if edad >= 60 else "")
    conteo[plan] += 1
    total += precios[plan]

print(total, conteo, max(conteo, key=conteo.get))