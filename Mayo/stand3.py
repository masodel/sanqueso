dias_semana = ["Lunes", "Martes", "Miércoles"]
NUM_DIAS = 3
NUM_STANDS = 4
NUM_PRODUCTOS = 3

print("=== Registro de ventas feria UAM ===\n")

total_general = 0.0  # Acumulador general

# Recorremos los días
for d in range(NUM_DIAS):
    print(f"\n {dias_semana[d]}")
    total_dia = 0.0  # Acumulador diario

    # Recorremos los stands del día
    for s in range(NUM_STANDS):
        productos = []  # Lista para guardar ventas de productos del stand
        print(f"\n   Stand {s+1}:")

        # Recorremos los productos del stand
        for p in range(NUM_PRODUCTOS):
            while True:
                try:
                    monto = float(input(f"    Producto {p+1} – Monto vendido: $ "))
                    if monto < 0:
                        print("     El monto no puede ser negativo.")
                        continue
                    productos.append(monto)  # Guardamos el monto
                    break
                except ValueError:
                    print("     Entrada inválida. Debes escribir un número.")

        # Sumamos los productos del stand
        total_stand = sum(productos[0:3])
        print(f"    Total del Stand {s+1}: ${total_stand:,.2f}")
        total_dia += total_stand

    # Mostrar total del día
    print(f"\n Total del día {dias_semana[d]}: ${total_dia:,.2f}")
    total_general += total_dia

# Mostrar total general
print("\n==============================")
print(f" TOTAL GENERAL DE LA FERIA: ${total_general:,.2f}")
print("==============================")