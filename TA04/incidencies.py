import csv
import xml.etree.ElementTree as ET

arrel = ET.Element("incidencies")

with open("incidencies.csv", "r", encoding="utf-8") as f:
    lector = csv.DictReader(f)

    for fila in lector:
        incidencia = ET.SubElement(arrel, "incidencia")

        for camp, valor in fila.items():
            camp_xml = camp.strip().replace(" ", "_").replace("?", "")
            node = ET.SubElement(incidencia, camp_xml)
            node.text = valor

arbre = ET.ElementTree(arrel)
arbre.write("incidencies.xml", encoding="utf-8", xml_declaration=True)

print("XML creat correctament!")
