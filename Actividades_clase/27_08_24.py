from Bio import ExPASy, SwissProt

# Ruta relativa hacia un archivo con datos de un gen
handle = open("./Actividades_clase/O23729.txt")
record = SwissProt.read(handle)
# Se busca el GN (gene name) en el archivo y se imprime
print(record.gene_name)

