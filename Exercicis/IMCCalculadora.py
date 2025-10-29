try:
    pes = float(input("Introdueix el teu pes en kg: "))
    altura = float(input("Introdueix la teva altura en metres: "))

    if altura <= 0:
        print("L'altura ha de ser un número positiu.")
    else:
        imc = pes / (altura ** 2)
        print(f"El teu IMC és: {imc:.2f}")

        if imc < 18.5:
            print("Estàs sota del pes ideal.")
        elif 18.5 <= imc <= 24.9:
            print("Estàs en el rang de pes normal.")
        else:
            print("Estàs sobre el pes ideal.")
except ValueError:
    print("Introdueix números vàlids per al pes i l'altura.")
