import sys
import datetime
from Classes.NCBIDataset import NCBIDataset

def ncbiDinuc(acc_file_name):
    acc_file_name = sys.argv[1]
    print(acc_file_name)

    acc_list = []
    try:
        with open(acc_file_name, "r") as fh:
            lines = fh.readlines()
            [acc_list.append(line.strip()) for line in lines]
            
        NCBIDataset().ncbiDatasets(acc_list)
    except Exception as e:
        with open("ncbi_dataset.log", 'a') as fh:
            now = datetime.now()
            fh.write(f"{str(e)}\t{now.strftime('%Y.%m.%d %H:%M:%S')}\n")
        
if __name__ == "__main__":
    ncbiDinuc(sys.argv[1])    
