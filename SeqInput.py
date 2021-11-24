import os
from Bio import SeqIO
from OligoCalcDB import dinucIndex

def seqInput():

    path = "C:\\Users\\hp\\source\\repos\\Sequencies\\Temp\\genome_assemblies_genome_fasta\\ncbi-genomes-2021-11-23\\"

    i = 1
    for file in os.listdir(path):
        for record in SeqIO.parse(path + file, "fasta"):
            print(f"{i} Dinuc calc in frames.")
            print(f"{record.id}\t{record.description}\t{len(record)}\t{record.seq[:20]}...{record.seq[-20:]}")
            dinucIndex(record)
            i += 1
        
    pass    


if __name__ == "__main__":
    seqInput()