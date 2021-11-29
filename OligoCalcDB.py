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
    dinucCountStr, _ = OligoDict().dinucDict(dinucDict, seqDinucLength)
    oligoDBDict.update(dinucCountStr)
   
    for key, value in oligoDBDict.items():
        print(f'{key}\t{value}')
        
    
    '''Calc frq and frq difference sum of dinucs in two frames of shuffled prime sequence.'''
    '''Shuffle prime sequences by MONO-nucleotides.'''
    dinucShuffleDiffSumList = []
    for _ in range(10):
        seqShuffle = SeqShuffle(seq).seqMonoShuffle() # Mononuc shuffle.
        dinucShuffleDict = OligoCountY(seqShuffle).oligoPosList()
        dinucShuffleDict = dict(sorted(dinucShuffleDict.items()))
        seqDinucLength = NucCalculate(str(seq.seq)).regexSeqLength() // 2
        _, dinucShuffleDiffSum = OligoDict().dinucDict(dinucShuffleDict, seqDinucLength)
        dinucShuffleDiffSumList.append(dinucShuffleDiffSum)
    
    dinucShuffleStr = [f'{item:.6f}' for item in dinucShuffleDiffSumList]
    dinucShuffleQueryStr = ', '.join(dinucShuffleStr)
    oligoDBDict.update({'mono_shuffle_diff': dinucShuffleQueryStr})
    print('Mono shuffle done.')
    
    '''Shuffle prime sequence by DI-nucleotides.'''
    dinucShuffleDiffSumList = []
    for _ in range(10):
        seqShuffle = SeqShuffle(seq).seqDiShuffle() # Dinuc shuffle.
        dinucShuffleDict = OligoCountY(seqShuffle).oligoPosList()
        dinucShuffleDict = dict(sorted(dinucShuffleDict.items()))
        seqDinucLength = NucCalculate(str(seq.seq)).regexSeqLength() // 2
        _, dinucShuffleDiffSum = OligoDict().dinucDict(dinucShuffleDict, seqDinucLength)
        dinucShuffleDiffSumList.append(dinucShuffleDiffSum)
        
    dinucShuffleStr = [f'{item:.6f}' for item in dinucShuffleDiffSumList]
    dinucShuffleQueryStr = ', '.join(dinucShuffleStr)
    oligoDBDict.update({'di_shuffle_diff': dinucShuffleQueryStr})
    print('Di shuffle done.')
    
    '''Shuffle prime sequence by TRI-nucleotides.'''
    dinucShuffleDiffSumList = []
    for _ in range(10):
        seqShuffle = SeqShuffle(seq).seqTriShuffle() # Trinuc shuffle.
        dinucShuffleDict = OligoCountY(seqShuffle).oligoPosList()
        dinucShuffleDict = dict(sorted(dinucShuffleDict.items()))
        seqDinucLength = NucCalculate(str(seq.seq)).regexSeqLength() // 2
        _, dinucShuffleDiffSum = OligoDict().dinucDict(dinucShuffleDict, seqDinucLength)
        dinucShuffleDiffSumList.append(dinucShuffleDiffSum)
        
    dinucShuffleStr = [f'{item:.6f}' for item in dinucShuffleDiffSumList]
    dinucShuffleQueryStr = ', '.join(dinucShuffleStr)
    oligoDBDict.update({'tri_shuffle_diff': dinucShuffleQueryStr})
    print('Tri shuffle done.')

    '''Write dinuc calc results dictionary to sql table.'''
    SeqMetaDB('dinucdb.sqlite3', 'dinuctbl').initTable()
    SQLQuery('dinucdb.sqlite3', 'dinuctbl').insertDict(oligoDBDict)
    