import xml.etree.ElementTree as ET
from collections import Counter
from colorama import Fore, Style, init
from datetime import datetime

# Inicialitza Colorama
init(autoreset=True)

# Llegeix el fitxer XML
arbre = ET.parse("incidencies.xml")
arrel = arbre.getroot()

# Comptadors
tipus_equip = Counter()
gravetat = Counter()
ubicacions = Counter()
solucio_previa = Counter()

total_valides = 0
total_invalides = 0

# PROCESSAR INCIDÈNCIES
for inc in arrel.findall("incidencia"):
    # Llegir dades
    data_text = inc.find("Data_detecció_de_la_incidència").text
    try:
        data = datetime.strptime(data_text, "%d/%m/%Y")
        if data.year > 2025:  # Exemple de filtre d’error
            total_invalides += 1
            continue
    except:
        total_invalides += 1
        continue

    tipus = inc.find("Tipus_de_equip").text
    gravetat_incidencia = inc.find("Grau_de_gravetat").text
    ubicacio = inc.find("Ubicació_equip_afectat").text
    solucio = inc.find("S-ha_intentat_alguna_solució_prèvia").text

    tipus_equip[tipus] += 1
    gravetat[gravetat_incidencia] += 1
    ubicacions[ubicacio] += 1
    solucio_previa[solucio] += 1
    total_valides += 1

# MOSTRAR RESULTATS
print(Fore.CYAN + "\n===== INFORME D'INCIDÈNCIES =====" + Style.RESET_ALL)
print(f"Total d’incidències vàlides: {total_valides}")
print(f"Total d’incidències descartades (errors): {total_invalides}\n")

print(Fore.YELLOW + " Incidències per tipus d’equip:" + Style.RESET_ALL)
for t, n in tipus_equip.items():
    print(f"  {t}: {n}")

print(Fore.YELLOW + "\n Incidències per gravetat:" + Style.RESET_ALL)
for g, n in gravetat.items():
    print(f"  {g}: {n}")

print(Fore.YELLOW + "\n Incidències per ubicació:" + Style.RESET_ALL)
for u, n in ubicacions.items():
    print(f"  {u}: {n}")

print(Fore.YELLOW + "\n Incidències amb solució prèvia:" + Style.RESET_ALL)
for s, n in solucio_previa.items():
    print(f"  {s}: {n}")

print(Fore.CYAN + "\n===== FI DE L'INFORME =====\n" + Style.RESET_ALL)

