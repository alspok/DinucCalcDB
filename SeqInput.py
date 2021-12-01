import os
from Bio import SeqIO
from OligoCalcDB import dinucIndex

def seqInput():

    base_path = "C:\\Users\\hp\\source\\repos\\Sequencies\\Procaryote\\Archaea\\ncbi-genomes-2021-11-24"

    i = 1
    for file in os.listdir(base_path):
        fpath = os.path.join(base_path, file)
        if not os.path.isdir(fpath):
            j = 1
            for record in SeqIO.parse(fpath, "fasta"):
                print(f"{i}-{j} Dinuc calc in frames.")
                dinucIndex(record)
                j += 1
            i += 1


if __name__ == "__main__":
    seqInput()