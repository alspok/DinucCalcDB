from collections import defaultdict
from Bio import SeqIO
from Classes.NucCalculate import NucCalculate
from Classes.OligoCountY import OligoCountY
from Classes.SeqMetaDB import SQLQuery, SeqMetaDB
from Classes.OligoDict import OligoDict

def dinucIndex(file_path, seq_name):
# def dinucIndex():
    print("Dinuc calc, result to SQL")
    # file_path = "C:\\Users\\hp\\source\\repos\\Sequencies\\"
    # # seq_name = "Bacteria\\Escherichia.coli.fasta"
    # # seq_name = "Bacteria\\Lactococcus.lactis.fasta"
    # # seq_name = "Test.fasta"
    # seq_name = "Test16.fasta"
    # # seq_name = "TestMono.fasta"
    
    seq = SeqIO.read(file_path + seq_name, 'fasta')
    
    oligoDBDict = defaultdict()
    oligoDBDict.update(OligoDict().headDict(seq))
    
    dinucDict = OligoCountY(str(seq.seq)).oligoPosList()
    dinucDict = dict(sorted(dinucDict.items()))
    # seqDinucLength = len(seq.seq) // 2
    seqDinucLength = NucCalculate(str(seq.seq)).regexSeqLength() // 2
    dinucCountStr = OligoDict().dinucDict(dinucDict, seqDinucLength)
    oligoDBDict.update(dinucCountStr)
   
    for key, value in oligoDBDict.items():
        print(f'{key}\t{value}')
        
    SeqMetaDB('dinucdb.sqlite3', 'dinuctbl').initTable()
    SQLQuery('dinucdb.sqlite3', 'dinuctbl').insertDict(oligoDBDict)
    
    pass
   
    
if __name__ == "__main__":
    dinucIndex()