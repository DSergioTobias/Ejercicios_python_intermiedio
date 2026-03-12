# Cafeteria
menu = {"cafe": 4000, "te": 3500, "jugo": 5000}

print("Café: $4000 | Té: $3500 | Jugo: $5000")

bebida = input("¿Qué bebida quieres? ")
cantidad = int(input("¿Cuántas unidades? "))

total = menu[bebida] * cantidad
print(f"Total a pagar: ${total}")