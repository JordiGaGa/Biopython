# ===========================================================================
# =                            imports
# ===========================================================================

from Bio import Entrez 
from pprint import pprint 
# ===========================================================================
# =                            Main
# ===========================================================================

Entrez.email= "jordigg@lcg.unam.mx"

# Analizar el las proteínas de la base de datos taxonomy
"""
handle = Entrez.esummary(db="taxonomy", id="9913,30521")
record = Entrez.read(handle)
print(len(record))
print(record[0].keys())
print(record[0]["Status"])
"""

#Buscar en otras bases de datos 
ids = "15718680,157427902"

record = Entrez.read(Entrez.elink(dbfrom="protein", id=ids,db='gene'))
pprint(record[0])


