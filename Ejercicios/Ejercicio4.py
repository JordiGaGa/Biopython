"""
Esto es un incremento de la tarea sobre búsqueda en pubmed:

Usaremos el archivo en el que guardamos los IDs de artículos de ciertx autorx y haremos lo siguiente:

Guardar en un nuevo archivo los abstracts de al menos tres artículos

Y por cada abstract guardado incluir los IDs (al menos 3) de los artículos que lo citan
"""

# ===========================================================================
# =                            imports
# ===========================================================================

from Bio import Entrez

# ===========================================================================
# =                            Main
# ===========================================================================
Entrez.email = "jordigg@lcg.unam.mx" # Correo

#Se creará archivo con los abstracts y IDs de citas en cas ode que haya, llamado "ID_citas.txt"
with open(r"C:\Users\jordi\OneDrive\Escritorio\Biopython\ID_citas.txt", 'w') as archivo_salida:
    # Se abre el archivo "IDs_articulos.txt" el cual ya tiene los IDs de los articulos con el 
    # autor buscado en el Ejercicio2.2.py
    with open(r"C:\Users\jordi\OneDrive\Escritorio\Biopython\IDs_articulos.txt", 'r') as f:
        for num, id_doc in enumerate(f): 
            handle = Entrez.efetch(db="pubmed", id=id_doc, rettype="abstract", retmode="text")
            data = handle.read()
            # Se agrega el abstract de cada ID del documento a "ID_citas.txt"
            archivo_salida.write(f"\n\n\n=======================ABSTRACT {num+1}========================\n\n\n" + data)
            handle.close()

            # SE BuscaN artículos que citen el artículo actual
            link_handle = Entrez.elink(dbfrom="pubmed", id=id_doc, linkname="pubmed_pubmed_citedin")
            records = Entrez.read(link_handle)
            link_handle.close()

            # Se Obtienen hasta 3 IDs de artículos que citen el artículo original (si hay)
            citas = []
            try:
                if records:
                    citas = [link["Id"] for link in records[0]["LinkSetDb"][0]["Link"][:3]]
            except IndexError:
                exit()

            # Añadir los IDs de los artículos citantes al archivo
            if citas:
                archivo_salida.write(f"\n\n=====IDs Articulos Citadores====\n".join(citas))
            else:
                archivo_salida.write("\n\n========Articulos no encontrados==========.\n")

            # Hay algunos casos en que no aparece ninguno de los 2 mensajes, mas no entendí por qué.