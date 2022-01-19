import sys
import datetime
from Classes.NCBIDataset import NCBIDataset
#from Classes.NCBIDataformat import NCBIDataformat
from Classes.DataSummary import DataSummary

"""Input access id info file items must be separated by tabs.
   [-2] item of line must be assembly number.
   [-1] item of line must bet seq length in bytes.
   # is first char of comment line separated from items by tab.
"""

# def ncbiDinuc(acc_file_name):
#     acc_file_name = sys.argv[1]
#     print(acc_file_name)
#     genome_length = 10**9
    
def ncbiDinuc():
    genome_length = 10**9
    acc_file_name = "Genomes\\Plants\\embryophyta"
    acc_file_name_long = "Genomes\\Plants\\embryophyta_long"
    print(acc_file_name)

    acc_list = []
    try:
        with open(acc_file_name, "r") as fh, open(acc_file_name_long, "w") as fhl:
            lines = fh.readlines()
            for line in lines:
                line_list = line.split("\t")
                if line_list[0] == "#":
                    continue
                else:
                    if int(line_list[-1]) <= genome_length:
                        acc_list.append(line_list[-2])
                    else:
                        fhl.write(line)
            
        acc_list_count = DataSummary().dataSummary(acc_list)
            
        # NCBIDataformat().ncbiDataformat(acc_list)    
        NCBIDataset().ncbiDatasets(acc_list, acc_list_count)
    except Exception as e:
        with open("ncbi_dataset.log", 'a') as fh:
            now = datetime.now()
            fh.write(f"{str(e)}\t{now.strftime('%Y.%m.%d %H:%M:%S')}\n")
        
if __name__ == "__main__":
    # ncbiDinuc(sys.argv[1])
    ncbiDinuc()
