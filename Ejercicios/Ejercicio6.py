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