"""
Utilice el archivo opuntia1.fasta, para realizar una busqueda en la base de datos de nr,
e imprima el titulo de la secuencia, su longitud y pvalue para aquellos alienamientos
con evalue < 0.05
"""
# ===========================================================================
# =                            imports
# ===========================================================================

import math
from Bio.Blast import NCBIWWW, NCBIXML
from Bio import SeqIO

# ===========================================================================
# =                            Main
# ===========================================================================

"""
Parte 1
"""
# Se toma el archivo en formato fasta que tenemos y guarda como record
record = SeqIO.read("./Ejercicios/opuntia1.fasta", format="fasta")
# Se hace la consulta a blastn en la base de datos nr del archivo 
result_handle = NCBIWWW.qblast("blastn", "nr", record.seq)

E_VALUE_THRESH = 0.05
blast_record = NCBIXML.read(result_handle)
for alignment in blast_record.alignments:
  for hsp in alignment.hsps:
    # Si los alineamientos tienen e value menor a .05 pasan 
    if hsp.expect < E_VALUE_THRESH:
      print("****Alignment****")
      print("sequence:", alignment.title)
      print("length:", alignment.length)
      # Fuente para obtener p value: https://www.ncbi.nlm.nih.gov/BLAST/tutorial/Altschul-1.html
      print("p value:", 1 - math.exp(-hsp.expect))
      print("score:",hsp.score)
      print(hsp.query[0:75] + "...")
      print(hsp.match[0:75] + "...")
      print(hsp.sbjct[0:75] + "...")
print("Listo")

"""
Parte 2
"""
# Se hace parseo del archivo y se hace lista con los fasta
secuencias = list(SeqIO.parse("./Ejercicios/opuntia.fasta", "fasta"))

E_VALUE_THRESH = 0.05

# Itera sobre cada secuencia del archivo FASTA
for record in secuencias:
    # Se toma el archivo en formato fasta que tenemos y guarda como record
    result_handle = NCBIWWW.qblast("blastn", "nr", record.seq)
    # Se hace la consulta a blastn en la base de datos nr del archivo 
    blast_record = NCBIXML.read(result_handle)

    # Variable para almacenar el mejor alineamiento
    best_alignment = None
    best_score = 0
    
    for alignment in blast_record.alignments:
        for hsp in alignment.hsps:
            # Si los alineamientos tienen e value menor a .05 y el 
            # score es mejor al último registrado pasan 
            if hsp.expect < E_VALUE_THRESH and hsp.score > best_score:
                best_score = hsp.score
                best_alignment = alignment
    
    # Imprime el alineamiento con el mejor score si existe y demás elementos
    if best_alignment:
        print("****Alignment****")
        print("sequence:", record.id)
        print("length:", best_alignment.length)
        print("score:",best_score)
    else:
        print(f"No se encontraron alineamientos con evalue < {E_VALUE_THRESH} para la secuencia {record.id}")

