import os
from Bio import SeqIO

def seqInput():

    path = "C:\\Users\\hp\\source\\repos\\Sequencies\\Temp\\genome_assemblies_genome_fasta\\ncbi-genomes-2021-11-23\\"

    for file in os.listdir(path):
        for record in SeqIO.parse(path + file, "fasta"):
            print(f"{record.id}\t{record.description}\t{len(record)}\t{record.seq[:50]}...{record.seq[-200:]}")
        
    pass    


if __name__ == "__main__":
    seqInput()