from Bio import Entrez
from pprint import pprint  # para mejor visualización de diccionarios!!
# Correo
Entrez.email = "jordigg@lcg.unam.mx"  # IMPORTANTE!!!
# handle con einfo
handle = Entrez.einfo()
result = handle.read() 
handle.close()
#chequemos qué hay en einfo 
print(result)