conteo = {"vainilla": 0, "chocolate": 0, "fresa": 0}

for i in range(1, 6):
    sabor = input(f"Cliente {i} - ¿Qué sabor quiere? (vainilla / chocolate / fresa): ")
    conteo[sabor] += 1

print("\n--- Resumen de pedidos ---")
for sabor, cantidad in conteo.items():
    print(f"{sabor}: {cantidad} veces")