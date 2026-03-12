edad = int(input("¿Cuántos años tienes? "))

if edad < 12:
    precio = 8000
elif edad <= 59:
    precio = 12000
else:
    precio = 9000

print(f"Total a pagar: ${precio}")