import xml.etree.ElementTree as ET
from collections import Counter
from colorama import Fore, Style, init
from datetime import datetime
import json
import os

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

# Llista amb incidències per guardar a JSON
incidencies_json = []

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
    correu = inc.find("Correo").text
    nom = inc.find("Nom_i_cognom").text
    marca = inc.find("Marca_temporal").text
    hora = inc.find("Hora_detecció_de_la_incidència").text
    com_detectat = inc.find("Com_s-ha_detectat_el_problema").text

    # Afegim a la llista JSON amb un ID únic
    incidencia_dict = {
        "ID": marca + "_" + correu,
        "Marca_temporal": marca,
        "Correo": correu,
        "Nom_i_cognom": nom,
        "Data_detecció": data_text,
        "Hora_detecció": hora,
        "Ubicació": ubicacio,
        "Tipus_de_equip": tipus,
        "Com_s-ha_detectat": com_detectat,
        "Solució_prèvia": solucio,
        "Gravetat": gravetat_incidencia
    }

    incidencies_json.append(incidencia_dict)

    # Comptadors per informe
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

# =============================
# GUARDAR EN JSON
# =============================
json_file = "incidencies.json"

if os.path.exists(json_file):
    print(Fore.MAGENTA + f"El fitxer {json_file} ja existeix." + Style.RESET_ALL)
    opc = input("Vols sobreescriure (s) o afegir noves incidències (a)? [s/a]: ").strip().lower()
    if opc == "s":
        with open(json_file, "w", encoding="utf-8") as f:
            json.dump(incidencies_json, f, indent=4, ensure_ascii=False)
        print(Fore.GREEN + "Fitxer sobreescrit correctament!" + Style.RESET_ALL)
    elif opc == "a":
        # Carreguem les incidències existents
        with open(json_file, "r", encoding="utf-8") as f:
            existents = json.load(f)

        # Evitem duplicats per ID
        ids_existents = {i["ID"] for i in existents}
        noves = [i for i in incidencies_json if i["ID"] not in ids_existents]

        existents.extend(noves)

        with open(json_file, "w", encoding="utf-8") as f:
            json.dump(existents, f, indent=4, ensure_ascii=False)

        print(Fore.GREEN + f"S'han afegit {len(noves)} noves incidències sense duplicats." + Style.RESET_ALL)
    else:
        print(Fore.RED + "Opció no vàlida. No s'ha fet cap canvi." + Style.RESET_ALL)
else:
    with open(json_file, "w", encoding="utf-8") as f:
        json.dump(incidencies_json, f, indent=4, ensure_ascii=False)
    print(Fore.GREEN + f"Fitxer {json_file} creat correctament amb totes les incidències." + Style.RESET_ALL)
