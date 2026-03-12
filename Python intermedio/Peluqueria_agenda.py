precios = {"corte": 0, "cepillado": 0, "tintura": 0}
conteo  = {"corte": 0, "cepillado": 0, "tintura": 0}
total_dia = 0

for i in range(1, 8):
    print(f"\nCliente {i}")
    nombre   = input("Nombre: ")
    servicio = input("Servicio (corte/cepillado/tintura): ")
    valor    = int(input("Valor pagado: $"))

    conteo[servicio]  += 1
    precios[servicio] += valor
    total_dia         += valor

print("\n===== Resumen =====")
print(f"Total del día: ${total_dia}")
for s in conteo:
    print(f"{s}: {conteo[s]} cliente(s) — ${precios[s]}")
print(f"\nServicio más solicitado: {max(conteo, key=conteo.get)}")