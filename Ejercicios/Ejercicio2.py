"""
Primera parte

Empleando Entrez.einfo y Entrez.read, imprime la descripción de los siguientes campos de la base de datos "protein":

FieldList "ECNO"
LinkList "protein_protein_small_genome"
Segunda parte

Automatizar lo siguiente:

Búsqueda con esearch de ciertx autorx y ciertas palabra en el título (con posibilidad de cambiar búsqueda) Ejemplo: J. Collado vides (como autor) Y ( regulon (en título del artículo) O regulación (en título del artículo) )

Guardar los IDs de los artículos en un archivo
"""

# ===========================================================================
# =                            imports
# ===========================================================================

from Bio import Entrez
from pprint import pprint  # para mejor visualización de diccionarios!!

# ===========================================================================
# =                            Main
# ===========================================================================
Entrez.email = "jordigg@lcg.unam.mx" # Correo
handle = Entrez.einfo(db = "protein") # indicar db (base de datos) de interes
record = Entrez.read(handle) #Se lee la base de datos 
"""
Primera parte
"""
# Obtener y mostrar la descripción del campo "ECNO"
for field in record["DbInfo"]["FieldList"]:
    if field["Name"] == "ECNO":
        print("Descripción de ECNO:",field["Description"])

# Obtener y mostrar la descripción del enlace "protein_protein_small_genome"
for link in record["DbInfo"]["LinkList"]:
    if link["Name"] == "protein_protein_small_genome":
        print("Descripción de protein_protein_small_genome:",link["Description"])

handle.close()
