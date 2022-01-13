from collections import defaultdict
import re

class OligoCountY():
    """Calc oligo position in seq using generator methods."""
    def __init__(self, seq: str) -> None:
        self.seq = seq.lower()
        self.dinuc_pos = defaultdict(list)
        self.oligo_range = range(2, 3)

    def oligoPosList(self):
        for olen in self.oligo_range:
            for pos, oligo in self.oligoSPosY(olen):
                if bool(re.match(r'[acgt]+$', oligo)):
                    self.dinuc_pos[oligo].append(pos)
        return self.dinuc_pos

    def oligoSPosY(self, olen):
        temp_seq = self.seq + self.seq[:olen]
        for i in range(0, len(temp_seq) - olen):
            yield i+1, temp_seq[i:i+olen]
