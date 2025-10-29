TIPUS_CANVI = 0.92

try:
    dolars = float(input("Introdueix la quantitat en dòlars: "))
except ValueError:
    print("Introdueix un número vàlid.")
else:
    euros = dolars * TIPUS_CANVI
    print(f"{dolars:.2f} $ equivalen a {euros:.2f} €")
finally:
    print("Conversió finalitzada.")
