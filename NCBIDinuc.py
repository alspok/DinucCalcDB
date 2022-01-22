import re
import datetime
from Classes.InitValues import InitValues as iv
from Classes.NCBIDataset import NCBIDataset
from Classes.DataSummary import DataSummary

"""
   Input access id info file items must be separated by tabs.
   File from https://www.ncbi.nlm.nih.gov/datasets/genomes.
   Filter columns assembly and size(Mb) as last and penultimate.
   [-2] second to last item in line must be assembly number.
   [-1] last item in line must bet seq length in bytes.
"""

# def ncbiDinuc(acc_file_name):
#     acc_file_name = sys.argv[1]
#     print(acc_file_name)
#     genome_length = 10**9

def ncbiDinuc():
    genome_length = 10**10
    
    """Init values from InitValues class"""
    acc_file_name = iv.path + iv.file_name
    acc_file_name_long = iv.path + iv.file_name_long
    
    # acc_file_name = "Genomes\\Test\\access_id"
    # acc_file_name_long = "Genomes\\Test\\access_id_long"
    print(acc_file_name)

    acc_list = []
    try:
        with open(acc_file_name, "r") as fh, open(acc_file_name_long, "w") as fhl:
            lines = fh.readlines()
            for line in lines:
                if line[0] == "#":
                    continue
                else:
                    line_list = line.split()
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
