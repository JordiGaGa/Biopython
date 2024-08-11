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

# Programa para contar y ver las keys de un campo (pubmed de python en concreto)
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
"""
# Código para hallar ciertos artículos en base a ciertos parámetros 
termino = "(Aedes[Title] OR Aedes[All Fields])AND((RNA-Seq[Title] XOR transcriptomic[Title]) OR (transcriptome[Title] OR sequencing[Title]))"
# Con OR da 171 y con XOR da 136
handle = Entrez.esearch(db="pubmed", term=termino)
result = Entrez.read(handle)
print(result["Count"])  #cuantos encontró
print(result["IdList"]) # lista de los primero 20
"""

#ESpell
#Obtengo la manera correcta de escribir mi pregunta.
"""
handle = Entrez.espell(term="biopythooon")
record = Entrez.read(handle)
print(record["Query"]) # lo que añadimos
print(record["CorrectedQuery"])
"""

#Esummary
# Es un submodulo que nos proporciona un resumen de la información de una lista de IDs:
"""
handle = Entrez.esummary(db="taxonomy", id="9913,30521")
record = Entrez.read(handle)
print(len(record))
print(record[1].keys())
print(record[1]["Id"])
"""

# pickle 
# Tamaño de archivos 
import pickle
## tamaño del record deseado
print(len(pickle.dumps(record))) #tamaño esummary