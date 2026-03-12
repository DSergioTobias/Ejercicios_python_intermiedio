edad = int(input("Ingresa tu edad: "))

if edad < 13:
    print(" No puedes ingresar al gimnasio.")
elif edad <= 17:
    print(" Perteneces a la clase JUVENIL (13 - 17 años).")
elif edad <= 59:
    print("Perteneces a la clase GENERAL (18 - 59 años).")
else:
    print("Perteneces a la clase SENIOR (60 años o más).")