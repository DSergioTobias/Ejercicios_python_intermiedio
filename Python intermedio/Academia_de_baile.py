clases = int(input("¿Cuántas clases asistió este mes? "))

if clases < 5:
    print("Asistencia: baja")
elif clases <= 8:
    print("Asistencia: media")
else:
    print("Asistencia: alta")