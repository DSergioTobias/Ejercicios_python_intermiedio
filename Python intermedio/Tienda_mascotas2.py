ventas = {"alimento": 0, "juguete": 0, "accesorio": 0}

for i in range(1, 11):
    print(f"\nVenta {i}")
    categoria = input("Categoría (alimento/juguete/accesorio): ")
    valor = int(input("Valor: $"))
    ventas[categoria] += valor

print("\n===== Resumen =====")
for categoria, total in ventas.items():
    print(f"{categoria}: ${total}")

print(f"\nMayor categoría: {max(ventas, key=ventas.get)}")