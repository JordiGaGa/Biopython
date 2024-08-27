"""
Segunda parte

Automatizar lo siguiente:

Búsqueda con esearch de ciertx autorx y ciertas palabra en el título (con posibilidad de cambiar búsqueda) Ejemplo: J. Collado vides (como autor) Y ( regulon (en título del artículo) O regulación (en título del artículo) )

Guardar los IDs de los artículos en un archivo
"""
# ===========================================================================
# =                            imports
# ===========================================================================

from Bio import Entrez

# ===========================================================================
# =                            functions
# ===========================================================================

# Función para realizar la búsqueda en PubMed
def Busqueda_articulos(autor, palabra1, palabra2):
    Entrez.email = "jordi.gg@lcg.unam.mx" 
    query = f'{autor}[Author] AND ({palabra1}[Title] OR {palabra2}[Title])'
    handle = Entrez.esearch(db="pubmed", term=query) 
    record = Entrez.read(handle)
    handle.close()
    return record['IdList']

# Función para guardar los IDs en un archivo
def Archivo_IDs(ids, filename):
    with open(filename, 'w') as f:
        for id in ids:
            f.write(f"{id}\n")


# ===========================================================================
# =                            Main
# ===========================================================================


autor = input("Introduce al autor: ")   # Autor a buscar "Lev Salnikov"
palabra1 = input("Introduce la primera palabra clave: ")   # 1° Palabra clave en el título "rejuvenation" 
palabra2 = input("Introduce la segunda palabra clave: ")   # 2° Palabra clave en el título "aging"
ids = Busqueda_articulos(autor, palabra1, palabra2)

# Guardar los IDs en un archivo
Archivo_IDs(ids, "IDs_articulos.txt")

print(f"Se han guardado {len(ids)} IDs en 'IDs_articulos.txt'.")