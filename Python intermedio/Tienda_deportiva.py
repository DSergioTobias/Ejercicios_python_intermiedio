contador = 0

for i in range(1, 7):
    precio = int(input(f"Precio del producto {i}: $"))
    if precio > 100000:
        contador += 1

print(f"\nProductos que cuestan más de $100.000: {contador}")