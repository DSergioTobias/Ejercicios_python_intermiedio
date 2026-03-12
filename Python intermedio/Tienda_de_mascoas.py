mascota = input("¿Qué tipo de mascota tienes? (perro / gato / conejo): ")

if mascota == "perro":
    print("Recomendación: Croquetas con proteína de pollo o res.")
elif mascota == "gato":
    print("Recomendación: Alimento húmedo con proteína de pescado.")
elif mascota == "conejo":
    print("Recomendación: Heno, verduras frescas y pellets.")
else:
    print("Mascota no reconocida.")