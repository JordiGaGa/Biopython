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
# handle con einfo
# Imprime como archivo XHML los datos 
"""
handle = Entrez.einfo()
result = handle.read() 
handle.close()
#chequemos qué hay en einfo 
print(result)
"""
"""
# Imprime como lista las bases de datos "['pubmed', 'protein', 'nuccore']"
handle = Entrez.einfo()
record = Entrez.read(handle)
# obtenemos diccionario (llave "Dblist")
print(record["DbList"][0:5])  # primeras 3 bases de datos
handle.close()
"""

handle = Entrez.einfo(db = "pubmed") # indicar db de interes
record = Entrez.read(handle)
"""
print(record["DbInfo"]["FieldList"])  # descripcion de pubmed
print(record["DbInfo"].keys())  # para saber qué podemos consultar
handle.close() #cerramos handle
"""
# imprimir todos los campos a los que podemos accesar de pubmed 
for field in record["DbInfo"]["FieldList"]:
  #print("%(Name)s, %(FullName)s, %(Description)s" % field)
  print(field["FullName"]+": "+field["Description"])
#Se imprime el URL de mi búsqueda
print(handle.url)