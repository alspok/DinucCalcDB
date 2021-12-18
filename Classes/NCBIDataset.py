import subprocess
import glob
from datetime import datetime
from Bio import SeqIO
from Classes.OligoCalcDB import OligoCalcDB

class NCBIDataset():

    def ncbiDatasets(self, acc_list):
        # acc_list = ["GCF_009729015.1", "GCF_000812185.1", "GCF_900177045.1"]
        for acc in acc_list:
            try:
                subprocess.run("datasets download genome accession " + acc +
                            " --exclude-protein " +
                            " --exclude-gff3 " +
                            " --exclude-genomic-cds"
                            " --exclude-rna ", shell=True)
                subprocess.run("tar xf ncbi_dataset.zip", shell=True)
                
                for file_name in glob.glob(".\\ncbi_dataset\\data\\" + acc + "\\" + acc + "*.fna"):
                    for seq_record in SeqIO.parse(file_name, "fasta"):
                        print(f"{seq_record}...\tlen {len(seq_record)}bp\n")
                        sr = type(seq_record)
                        srs = type(seq_record.seq)
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
    
def ncbiDataset():
        
    acc_list = ["GCF_009729015.1", "GCF_000812185.1", "GCF_900177045.1"]
    NCBIDataset().ncbiDatasets(acc_list)


if __name__ == "__main__":
    ncbiDataset()