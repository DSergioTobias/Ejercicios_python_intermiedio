precios = {"cono": 3000, "vaso": 4000, "banana split": 9000}
conteo = {"cono": 0, "vaso": 0, "banana split": 0}
total_vendido = 0
clientes = 0

while input("\n¿Atender cliente? (si/no): ") == "si":
    producto = input("Producto (cono/vaso/banana split): ")
    cantidad = int(input("Cantidad: "))
    conteo[producto] += cantidad
    total_vendido += precios[producto] * cantidad
    clientes += 1

print(f"\nClientes: {clientes}")
print(f"Total vendido: ${total_vendido}")
print(f"Más pedido: {max(conteo, key=conteo.get)}")