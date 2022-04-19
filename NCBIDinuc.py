import os
from datetime import datetime
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
def ncbiDinuc():
    dir_list = os.listdir(iv.path)
    for acc_file in dir_list:
        if acc_file.endswith(".acc"):
            acc_file_name = iv.path + acc_file
            print(acc_file_name)

        # accession number in file line must be second last. first last seq length.
        acc_list = []
        try:
            with open(acc_file_name, "r") as fh:
                lines = fh.readlines()
                for line in lines:
                    line = line.strip()
                    if line.startswith("#") or line.startswith("\n"):
                        continue
                    else:
                        line_list = line.split("\t")
                        acc_list.append(line_list[-2]) # accession number in file line must be second last. first last seq length.
                
            acc_list_count = DataSummary().dataSummary(acc_list)
            NCBIDataset().ncbiDatasets(acc_list, acc_list_count)
        except Exception as e:
            print(f"Exeption from main: {e}")
        
if __name__ == "__main__":
    # ncbiDinuc(sys.argv[1])
    ncbiDinuc()
