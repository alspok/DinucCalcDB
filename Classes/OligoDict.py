import re
from collections import defaultdict
from Classes.NucCalculate import NucCalculate
from Bio import Seq

class OligoDict():
    def __init__(self) -> None:
        pass
            
    def headDict(self, seq: object, acc_name) -> dict:
        head = defaultdict()
        rSeqLength = NucCalculate(str(seq.seq)).regexSeqLength()
        
        head.update({'access_name': acc_name,
                     'seq_name': seq.id,
                     'description': seq.description,
                    #  'seq_length': f'{len(seq.seq)} bp',
                     'seq_length': f'{rSeqLength} bp'
                    })
                     
        monoNuc = NucCalculate(seq.seq.lower()).nucCalc()
        head.update({'gc_percent': f'{((monoNuc[1] + monoNuc[2]) / rSeqLength * 100):.2f} %'}) 
        
        return head
    
    def dinucDict(self, dinucDict: dict, dinucLength: int) -> dict:
        dinucCountDict = defaultdict()
        for key, value in dinucDict.items():
            count = [0]*3
            for val in value:
                if val % 2 != 0: count[0] += 1
                if val % 2 == 0: count[1] += 1
            count[2] = abs(count[0] - count[1])
            dinucCountDict[key] = count
            
        dinucDiffSum = 0
        for value in dinucCountDict.values():
            dinucDiffSum += value[2] / dinucLength
        
        dinucCountStr = defaultdict()
        for key, value in dinucCountDict.items():
            scount = ['']*3
            scount[0] = f'{value[0] / dinucLength:.4f}'
            scount[1] = f'{value[1] / dinucLength:.4f}'
            scount[2] = f'{abs(value[0] / dinucLength - value[1] / dinucLength):.6f}'
            dinucCountStr[key] = scount

        for key, value in dinucCountStr.items():
            svalue = ', '.join(value)
            dinucCountStr[key] = svalue
            
        dinucCountStr.update({'di_diff': f'{dinucDiffSum:.6f}'})
        
        return dinucCountStr, dinucDiffSum
        
    