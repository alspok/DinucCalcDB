from collections import defaultdict
from Classes.InitValues import InitValues as iv
from Classes.OligoCountY import OligoCountY
from Classes.NucCalculate import NucCalculate
from Classes.SeqMetaDB import SQLQuery, SeqMetaDB
from Classes.OligoDict import OligoDict
from Classes.SeqShuffle import SeqShuffle

class OligoCalcDB():

    def dinucIndex(self, seq: object, acc_name) -> None:
        
        oligoDBDict = defaultdict()
        oligoDBDict.update(OligoDict().headDict(seq, acc_name))
        shuffle_mono = iv.shuffle_mono
        shuffle_di = iv.shuffle_di
        shuffle_tri = iv.shuffle_tri
        shuffle_quantity = iv.shuffle_quantity
        # shuffle_mono = 3 # Mononuc shuffle.
        # shuffle_di = 3 # Dinuc shuffle.
        # shuffle_tri = 3 # Trinuc shuffle.
        # shuffle_quantity = shuffle_mono + shuffle_di + shuffle_tri # Seq shuffle quantity sum.
        
        '''Calc frq and frq difference sum of dinucs in two frames.'''
        dinucDict = OligoCountY(str(seq.seq)).oligoPosList()
        dinucDict = dict(sorted(dinucDict.items()))
        seqDinucLength = NucCalculate(str(seq.seq)).regexSeqLength() // 2
        dinucCountStr, _ = OligoDict().dinucDict(dinucDict, seqDinucLength)
        oligoDBDict.update(dinucCountStr)
    
        for key, value in oligoDBDict.items():
            if key == "seq_name" or key == "description" or key == "seq_length" or key == "assembly_name":
                continue
            else:
                print(f'{key}\t{value}')
        
        """Calc frq and frq difference sum of dinucs in two frames of shuffled prime sequence."""
        """Shuffle prime sequences by MONO-nucleotides."""
        dinucShuffleDiffSumList = []
        for i in range(shuffle_mono):
            print(f"Suffle mononuc [{i+1} of {shuffle_mono}] of {shuffle_quantity}", end="\r", flush=True)
            seqShuffle = SeqShuffle(seq).seqMonoShuffle() # Mononuc shuffle.
            dinucShuffleDict = OligoCountY(seqShuffle).oligoPosList()
            dinucShuffleDict = dict(sorted(dinucShuffleDict.items()))
            seqDinucLength = NucCalculate(str(seq.seq)).regexSeqLength() // 2
            _, dinucShuffleDiffSum = OligoDict().dinucDict(dinucShuffleDict, seqDinucLength)
            dinucShuffleDiffSumList.append(dinucShuffleDiffSum)
        print("")
        dinucShuffleStr = [f'{item:.6f}' for item in dinucShuffleDiffSumList]
        dinucShuffleQueryStr = ', '.join(dinucShuffleStr)
        oligoDBDict.update({'mono_shuffle_diff': dinucShuffleQueryStr})
        
        """Shuffle prime sequence by DI-nucleotides."""
        dinucShuffleDiffSumList = []
        for i in range(shuffle_di):
            print(f"Suffle dinuc [{i+1} of {shuffle_di}] of {shuffle_quantity}", end="\r", flush=True)
            seqShuffle = SeqShuffle(seq).seqDiShuffle() # Dinuc shuffle.
            dinucShuffleDict = OligoCountY(seqShuffle).oligoPosList()
            dinucShuffleDict = dict(sorted(dinucShuffleDict.items()))
            seqDinucLength = NucCalculate(str(seq.seq)).regexSeqLength() // 2
            _, dinucShuffleDiffSum = OligoDict().dinucDict(dinucShuffleDict, seqDinucLength)
            dinucShuffleDiffSumList.append(dinucShuffleDiffSum)
        print("")
        dinucShuffleStr = [f'{item:.6f}' for item in dinucShuffleDiffSumList]
        dinucShuffleQueryStr = ', '.join(dinucShuffleStr)
        oligoDBDict.update({'di_shuffle_diff': dinucShuffleQueryStr})
        
        """Shuffle prime sequence by TRI-nucleotides."""
        dinucShuffleDiffSumList = []
        for i in range(shuffle_tri):
            print(f"Shuffle trinuc [{i+1} of {shuffle_tri}] of {shuffle_quantity}", end="\r", flush=True)
            seqShuffle = SeqShuffle(seq).seqTriShuffle() # Trinuc shuffle.
            dinucShuffleDict = OligoCountY(seqShuffle).oligoPosList()
            dinucShuffleDict = dict(sorted(dinucShuffleDict.items()))
            seqDinucLength = NucCalculate(str(seq.seq)).regexSeqLength() // 2
            _, dinucShuffleDiffSum = OligoDict().dinucDict(dinucShuffleDict, seqDinucLength)
            dinucShuffleDiffSumList.append(dinucShuffleDiffSum)
        print("")
        dinucShuffleStr = [f'{item:.6f}' for item in dinucShuffleDiffSumList]
        dinucShuffleQueryStr = ', '.join(dinucShuffleStr)
        oligoDBDict.update({'tri_shuffle_diff': dinucShuffleQueryStr})
        print('\n')

        '''Write dinuc calc results dictionary to sql table.'''
        # SeqMetaDB('dinucdb.sqlite3', 'dinuctbl').initTable()
        # SQLQuery('dinucdb.sqlite3', 'dinuctbl').insertDict(oligoDBDict)
        
        SeqMetaDB(iv.dbname, iv.dbtable).initTable()
        SQLQuery(iv.dbname, iv.dbtable).insertDict(oligoDBDict)
    