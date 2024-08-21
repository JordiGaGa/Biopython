"""
1. Genera una consulta con Entrez.einfo a la base de datos de pubmed, para imprimir el nombre y la descripción de todos los FieldList

2.  Repite la consulta anterior, pero sin usar un iterador, imprime la descripción solo del primer elemento de la lista de los FieldList.
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
handle = Entrez.einfo(db = "pubmed") # indicar db (base de datos) de interes
record = Entrez.read(handle) #Se lee la base de datos 

# Imprimir cada Name, FullName y Description de los elementos de la base de datos
for field in record["DbInfo"]["FieldList"]:
  print(field["Name"], field["FullName"]+": "+field["Description"])

# Imprimir sólo el primer elemento de la lista Fiedlist
for field in record["DbInfo"]["FieldList"]:
  if field["Name"] == "ALL":
    print(field["Description"])
    exit

handle.close()