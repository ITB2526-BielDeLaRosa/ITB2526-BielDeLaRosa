def calcular_factura():
    print("=== Càlcul de la factura de l'aigua ===")

    try:
        litres = float(input("Introdueix els litres d'aigua consumits: "))

        quota_fixa = 6.0  # euros
        quota_variable = 0.0

        if litres < 0:
            print("El consum no pot ser negatiu.")
            return

        if litres < 50:
            quota_variable = 0.0
        elif litres <= 200:
            quota_variable = litres * 0.1
        else:
            quota_variable = litres * 0.3

        total = quota_fixa + quota_variable

        print(f"\n--- Resum de la factura ---")
        print(f"Consum: {litres} litres")
        print(f"Quota fixa: {quota_fixa:.2f} €")
        print(f"Quota variable: {quota_variable:.2f} €")
        print(f"Import total: {total:.2f} €")

    except ValueError:
        print("Error: Has d'introduir un número vàlid.")


def menu():
    while True:
        print("\n===== MENÚ PRINCIPAL =====")
        print("1. Calcular factura de l'aigua")

        opcio = input("Tria la opció (1): ")

        if opcio == "1":
            calcular_factura()
        else:
            print("Opció no vàlida. Torna-ho a intentar.")


# Executar el programa
menu()
