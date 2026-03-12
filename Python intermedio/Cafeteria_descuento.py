precios = {"cafe": 4000, "capuchino": 7000, "pastel": 6000}
total_dia = 0

while True:
    producto = input("\nProducto (cafe/capuchino/pastel) o 'salir': ")
    if producto == "salir":
        break

    cantidad = int(input("Cantidad: "))
    subtotal = precios[producto] * cantidad

    if subtotal > 20000:
        descuento = subtotal * 0.10
        total = subtotal - descuento
        print(f"Subtotal: ${subtotal} - Descuento 10%: ${descuento:.0f} → Total: ${total:.0f}")
    else:
        total = subtotal
        print(f"Total: ${total}")

    total_dia += total

print(f"\nTotal acumulado del día: ${total_dia:.0f}")