from Bio.Blast import NCBIWWW
from Bio import SeqIO
#help(NCBIWWW.qblast)

# Puede recibir el ID o la secuencia 
#result_handle = NCBIWWW.qblast("blastn", "nt", "8332116")

record = SeqIO.read("./Actividades_clase/m_cold.fasta.txt", format="fasta")
result_handle = NCBIWWW.qblast("blastn", "nt", record.seq)
result_handle

#Desde python podemos utilizar el módulo subprocess para ejecutar una linea de comando :
"""
import subprocess
cmd = "blastx -query opuntia.fasta -db nr -out opuntia.xml"
cmd += " -evalue 0.001 -outfmt 5"
subprocess.run(cmd, shell=True)
"""