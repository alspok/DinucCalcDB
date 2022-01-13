import random

class SeqShuffle():
    def __init__(self, seq: str) -> None:
        self.seq_list = list(seq)
        
    def seqMonoShuffle(self) -> str:
        # self.seq_list.append(self.seq_list[-1])
        random.shuffle(self.seq_list)
        return ''.join(self.seq_list)
    
    def seqDiShuffle(self) -> str:
        di = [self.seq_list[i] + self.seq_list[i+1] for i in range(0, (len(self.seq_list) - 1), 2)]
        random.shuffle(di)
        return ''.join(di)
    
    def seqTriShuffle(self) -> str:
        tri = [self.seq_list[i] + self.seq_list[i+1] + self.seq_list[i+2] for i in range(0, (len(self.seq_list) - 2), 3)]
        random.shuffle(tri)
        return ''.join(tri)