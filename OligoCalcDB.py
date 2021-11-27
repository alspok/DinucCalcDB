from collections import defaultdict
from Bio import SeqIO
from Classes.NucCalculate import NucCalculate
from Classes.OligoCountY import OligoCountY
from Classes.SeqMetaDB import SQLQuery, SeqMetaDB
from Classes.OligoDict import OligoDict
from Classes.SeqShuffle import SeqShuffle

def dinucIndex(seq: object) -> None:
    
    oligoDBDict = defaultdict()
    oligoDBDict.update(OligoDict().headDict(seq))
    
    '''Calc frq and frq difference sum of dinucs in two frames.'''
    dinucDict = OligoCountY(str(seq.seq)).oligoPosList()
    dinucDict = dict(sorted(dinucDict.items()))
    seqDinucLength = NucCalculate(str(seq.seq)).regexSeqLength() // 2
    dinucCountStr = OligoDict().dinucDict(dinucDict, seqDinucLength)
    oligoDBDict.update(dinucCountStr)
   
    for key, value in oligoDBDict.items():
        print(f'{key}\t{value}')
        
    SeqMetaDB('dinucdb.sqlite3', 'dinuctbl').initTable()
    SQLQuery('dinucdb.sqlite3', 'dinuctbl').insertDict(oligoDBDict)
    
    '''Calc frq and frq difference sum of dinucs in two frames of shuffled prime sequence.
    Shuffle sequences by mono- and di-nucleotides.'''
    for _ in range(10):
        seqShuffle = SeqShuffle(seq).seqMonoShuffle()
        dinucShuffleDict = OligoCountY(seqShuffle).oligoPosList()
    
    
    pass
   
    
if __name__ == "__main__":
    dinucIndex()