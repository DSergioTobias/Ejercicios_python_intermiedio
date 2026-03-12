tarifas = {"carro": 4000, "moto": 2000}
carros, motos = 0, 0
total_recaudado = 0
max_pago = 0
placa_max = ""

for i in range(1, 9):
    print(f"\nVehículo {i}")
    placa = input("Placa: ")
    tipo = input("Tipo (carro/moto): ")
    horas = int(input("Horas parqueado: "))

    pago = tarifas[tipo] * horas
    total_recaudado += pago

    if tipo == "carro":
        carros += 1
    else:
        motos += 1

    if pago > max_pago:
        max_pago = pago
        placa_max = placa

    print(f"Total a pagar: ${pago}")

print(f"\n===== Resumen =====")
print(f"Total recaudado: ${total_recaudado}")
print(f"Carros: {carros} | Motos: {motos}")
print(f"Mayor pago: {placa_max} con ${max_pago}")