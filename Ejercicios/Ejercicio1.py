# ===========================================================================
# =                            imports
# ===========================================================================

from Bio import Entrez
from pprint import pprint  # para mejor visualización de diccionarios!!

# ===========================================================================
# =                            Main
# ===========================================================================

Entrez.email = "jordigg@lcg.unam.mx" # Correo
handle = Entrez.einfo(db = "pubmed") # indicar db de interes
record = Entrez.read(handle)
"""
for field in record["DbInfo"]["FieldList"]:
  #print("%(Name)s, %(FullName)s, %(Description)s" % field)
  print(field["Name"], field["FullName"]+": "+field["Description"])
"""
# Imprimir sólo el primer elemento de la lista Fiedlist
for field in record["DbInfo"]["FieldList"]:
  if field["Name"] == "ALL":
    print(field["Description"])
    exit