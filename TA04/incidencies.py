import csv
import xml.etree.ElementTree as ET

# Crear arrel XML
arrel = ET.Element("incidencies")

# Obrir CSV
with open("incidencies.csv", "r", encoding="utf-8") as f:
    lector = csv.DictReader(f)
    for fila in lector:
        incidencia = ET.SubElement(arrel, "incidencia")
        for camp, valor in fila.items():
            node = ET.SubElement(incidencia, camp.replace(" ", "_"))
            node.text = valor

# Guardar XML
arbre = ET.ElementTree(arrel)
arbre.write("incidencies.xml", encoding="utf-8", xml_declaration=True)
print("XML creat correctament!")
