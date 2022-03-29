import subprocess
import json

class DataSummary():
    
    def dataSummary(self, acc_list) -> int:
        acc_count = 0
        
        for acc in acc_list:
            subprocess.run(".\\bin\\datasets summary genome accession " + acc + "  > summary.json", shell=True)
            
            #subprocess.run(datasets_query, shell=True)
            # with open("summary.json", "r") as json_fh:
            with open('summary.json', 'r', encoding="cp437", errors='ignore') as json_fh:
                json_object = json.load(json_fh)
            
            try:
                for asmbl in json_object["assemblies"]:
                    acc_count += len(asmbl["assembly"]["chromosomes"])
            except Exception as e:
                print(e)
        
        return acc_count