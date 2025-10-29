try:
    preuOriginal = float(input("Diga'm el preu original de l'article: "))
    descompte = float(input("Diga'm el descompte que ofereix en percentatge: "))
except ValueError:
    print("Introdueix-me un número vàlid.")
else:
    preuFinal = preuOriginal - (preuOriginal * descompte / 100)
    print("El preu final de l'article és:", preuFinal)
finally:
    print("Gràcies per utilitzar el programa.")
