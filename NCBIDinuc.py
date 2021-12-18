import sys
from Classes.NCBIDataset import NCBIDataset

acc_file_name = sys.argv[1]
print(acc_file_name)

acc_list = []
with open(acc_file_name, "r") as fh:
    lines = fh.readlines()
    [acc_list.append(line.strip()) for line in lines]
    
NCBIDataset().ncbiDatasets(acc_list)
