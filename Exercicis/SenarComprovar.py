try:
    numero = int(input("Introdueix un número sencer: "))
except ValueError:
    print("Introdueix un número vàlid.")
else:
    if numero % 2 == 0:
        print(f"El número {numero} és parell.")
    else:
        print(f"El número {numero} és senar.")
finally:
    print("Comprovació finalitzada.")
