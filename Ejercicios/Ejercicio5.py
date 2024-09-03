"""
Buscar el accession de la base de datos de UniProtKB del gen DEFA del mosquito Aedes aegypti
"""

# ===========================================================================
# =                            imports
# ===========================================================================

from Bio import Entrez, SeqIO

# ===========================================================================
# =                            Main
# ===========================================================================
Entrez.email = "jordigg@lcg.unam.mx" # Correo

# Se busca en la base de datos protein el término a buscar
handle = Entrez.esearch(db = "protein", term = "DEFA AND Aedes aegypti[Orgn]")
record = Entrez.read(handle)
# Tomo el primer elemento del IdList
prot_id = record["IdList"][0]
print(prot_id)
# Busco ese elemento en la base de datos protein 
handle =  Entrez.efetch(db="protein", id=prot_id, rettype="gb", retmode="text")
record = SeqIO.read(handle, "genbank")
handle.close()
# Se ve la información de la proteina y organismo en este caso en otras bases de datos
db_source = record.annotations['db_source']
print(db_source)