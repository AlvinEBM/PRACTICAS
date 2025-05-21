disponible = {100: 3, 50: 6, 20: 10, 10: 50, 1: 50}

# Retorna la cantidad total de dinero disponible
def cantidad_disponible():
    total = 0
    for k, v in disponible.items():
        total += k * v
    return total

# Calcula cuántos billetes se pueden usar de una denominación sin exceder el saldo
def get_denominacion(denominacion, saldo):
    count = saldo // denominacion
    if count > disponible[denominacion]:
        count = disponible[denominacion]
    disponible[denominacion] -= count
    return count

# Realiza el retiro del monto solicitado
def retirar(monto):
    global disponible  # por si deseas modificar desde fuera luego
    if monto > cantidad_disponible():
        print("No hay efectivo suficiente para retirar el monto")
        return

    retiro = {}  # Para registrar lo que se va retirando
    saldo = monto

    # Ordenamos las denominaciones de mayor a menor
    for k in sorted(disponible.keys(), reverse=True):
        if saldo <= 0:
            break
        count = get_denominacion(k, saldo)
        if count > 0:
            retiro[k] = count
            saldo -= k * count

    if saldo > 0:
        print("No se puede retirar el monto exacto con las denominaciones disponibles.")
        return

    print(f"Retiro exitoso de {monto}. Se entregaron:")
    for k, count in retiro.items():
        print(f"{count} billetes/monedas de {k}")

# Ejecución
print("Total disponible antes del retiro:", cantidad_disponible())
monto = 1300
retirar(monto)
print("Total disponible después del retiro:", cantidad_disponible())
