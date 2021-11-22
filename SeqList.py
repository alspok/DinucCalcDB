import os
from OligoCalcDB import dinucIndex

def seqList():
    path = "C:\\Users\\hp\\source\\repos\\Sequencies\\Bacteria\\"
    files = os.listdir(path)
    
    i = 1
    for file in files:
        print(i, end='  ')
        dinucIndex(path, file)
        i += 1
    
if __name__ == "__main__":
    seqList()