# ===========================================================================
# =                            imports
# ===========================================================================

from Bio import Entrez
from pprint import pprint  # para mejor visualización de diccionarios!!

# ===========================================================================
# =                            Main
# ===========================================================================

# Correo
Entrez.email = "jordigg@lcg.unam.mx"  # IMPORTANTE!!!
handle = Entrez.esearch(db = "pubmed", term = "biopython")
record = Entrez.read(handle)
""" 
print(record["Count"])
print(record.keys())
handle.close()
"""

#Programa para consultar publicaciones de un autor
"""
handle = Entrez.esearch(db="pubmed", term='Mateo-Estrada V',field='AUTH')
record = Entrez.read(handle)
print(handle.url)  # URL de request
print(record["IdList"])  # ids de artículos
print(record["Count"])
handle.close()
"""


