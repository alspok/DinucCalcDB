import os
from Bio import SeqIO
from OligoCalcDB import dinucIndex

def seqInput():

    path = "C:\\Users\\hp\\source\\repos\\Sequencies\\Temp\\ncbi-genomes-2021-11-24\\"

    i = 1
    for file in os.listdir(path):
        j = 1
        for record in SeqIO.parse(path + file, "fasta"):
            print(f"{i}-{j} Dinuc calc in frames. {record.description}\t{len(record)}")
            dinucIndex(record)
            j += 1
        i += 1
        
    pass    


if __name__ == "__main__":
    seqInput()