import re

class NucCalculate():
    
    def __init__(self, seq: str) -> None:
        self.seq = seq.lower()
        self.nucs = ['a', 'c', 'g', 't']
    
    def nucCalc(self) -> list:
        monoNuc = []
        for nuc in self.nucs:
            monoNuc.append(self.seq.count(nuc))
            
        return monoNuc
    
    def regexSeqLength(self) -> int:
        return len(re.findall(r'[acgt]', self.seq))