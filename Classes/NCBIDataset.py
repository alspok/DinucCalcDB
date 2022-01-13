import subprocess
import os
import glob
from datetime import datetime
from Bio import SeqIO
from Classes.OligoCalcDB import OligoCalcDB

class NCBIDataset():

    def ncbiDatasets(self, acc_list: list, acc_list_count: int):
        
        for acc in acc_list:
            try:
                subprocess.run(".\\bin\\datasets download genome accession " + acc +
                            " --exclude-protein " +
                            " --exclude-gff3 " +
                            " --exclude-genomic-cds" +
                            " --exclude-rna ", shell=True)
                subprocess.run("tar xf ncbi_dataset.zip", shell=True)
                
                wdir = ".\\ncbi_dataset\\data\\" + acc + "\\"
                wdir_files = os.listdir(wdir)
                sub_wdir_files = []
                for sub_file in wdir_files:
                    if sub_file.find(acc) != -1 or sub_file.find("chr") != -1:
                        sub_wdir_files.append(f"{wdir}{sub_file}")
                current_count = 1
                for file_name in sub_wdir_files:
                    for seq_record in SeqIO.parse(file_name, "fasta"):
                        if seq_record.description.find("plasmid") > -1: #Bypass plasmids in seq description
                            continue
                        print(f"\nCalculating {current_count} of {acc_list_count}")
                        current_count += 1
                        print(f"{seq_record}\tlen {len(seq_record)}bp")
                        OligoCalcDB().dinucIndex(seq_record)
                    # with open(file_name, 'r') as fh:
                    #     print(acc)
                    #     print(fh.read(200) + '...')
                        
                subprocess.run("del ncbi_dataset.zip", shell=True)
                subprocess.run("rmdir /s /q ncbi_dataset", shell=True)
            except Exception as e:
                # error_msg = "Oops!" + e.__class__ + "occurred."
                error_msg = str(e)
                print(error_msg)
                with open("ncbi_dataset.log", 'a') as fh:
                    now = datetime.now()
                    fh.write(f"{error_msg}\t{now.strftime('%Y.%m.%d %H:%M:%S')}\n")
                
        pass
    
# def ncbiDataset():
        
#     acc_list = ["GCF_009729015.1", "GCF_000812185.1", "GCF_900177045.1"]
#     NCBIDataset().ncbiDatasets(acc_list)


# if __name__ == "__main__":
#     ncbiDataset()