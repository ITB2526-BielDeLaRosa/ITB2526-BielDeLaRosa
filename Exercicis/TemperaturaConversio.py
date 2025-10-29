try:
    celsius = float(input("Introdueix la temperatura en graus Celsius: "))
except ValueError:
    print("Introdueix un número vàlid.")
else:
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius:.2f} °C equivalen a {fahrenheit:.2f} °F")
