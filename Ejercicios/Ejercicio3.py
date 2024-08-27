"""
búsqueda de linajes. Busquemos qué tan emparentados están dos organismos con las herramientas que hemos visto.

Usaremos a Notoryctes typhlops y Chrysochloris asiatica

Como nuestra pregunta es sobre linajes, la base de datos que usaremos será Taxonomy.

PRIMERA PARTE: Hacer una búsqueda con esearch (en este caso contamos con 
#los nombres de los organismos), la búsqueda nos dará su ID.
SEGUNDA PARTE: Usar el ID para obtener archivo con el linale de cada topo.
Contesta la pregunta:  En que punto divergen sus linajes.
Punto Opcional:  ¿como compararías ambas linajes para que la respuesta fuera automática?
"""
# ===========================================================================
# =                            imports
# ===========================================================================

from Bio import Entrez

# ===========================================================================
# =                            functions
# ===========================================================================

# Se crea archivo con IDs obtenidos de los 2 organismos
def Archivo_IDs(ids, filename):
    with open(filename, 'w') as f:
        for id in ids:
            f.write(f"{id}\n")

# ===========================================================================
# =                            Main
# ===========================================================================
Entrez.email = "jordigg@lcg.unam.mx" # Correo
# Introducir base de datos y organismos a checar (diferentes obviamente)
handle = Entrez.esearch(db = "Taxonomy", term="Notoryctes typhlops[Orgn] OR Chrysochloris asiatica[Orgn]")
# Indicar db (base de datos) de interes
record = Entrez.read(handle)
ids = record["IdList"]
filename = "IDs_organisms.txt"

Archivo_IDs(ids, filename)
print(f"Se ha creado archivo {filename} con los ID de los organismos")
# Se abre el archivo y se lee
with open(filename, 'r') as f:
    org1 = 0
    for num, id_taxo in enumerate(f):
        handle2 = Entrez.efetch(db="Taxonomy", id=id_taxo, retmode="xml")
        # Se queda el segundo organismo
        org2 = Entrez.read(handle2)
        if num == 0:
            # Se guarda el primer organismo
            org1 = org2[0]["Lineage"]
        tax1 = org1.split(";")
        tax2 = org2[0]["Lineage"].split(";") 
        min_len = min(len(tax1), len(tax2))
        # Se analiza la longitud en palabras de ambos para tomar la mínima para el ciclo for
        
        for i in range(min_len): 
            if tax1[i] != tax2[i]: 
                print(f"Los organismos difieren a partir de la categoría {tax1[i-1]}")
                exit()
       
       












