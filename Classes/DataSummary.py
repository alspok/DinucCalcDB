import subprocess
import json

class DataSummary():
    
    def dataSummary(self, acc_list) -> int:
        acc_count = 0
        
        for acc in acc_list:
<<<<<<< HEAD
            subprocess.run(".\\bin\\datasets summary genome accession " + acc + "  > summary.json", shell=True)
=======
            subprocess.run(".\\bin\\datasets summary genome accession " + acc + " > summary.json", shell=True)
>>>>>>> 266d18afb6b48fe967d9f0d127a4eb7a7ccfa0ad
            
            #subprocess.run(datasets_query, shell=True)
            with open("summary.json", "r") as json_file:
                json_object = json.load(json_file)
            
            for asmbl in json_object["assemblies"]:
                acc_count += len(asmbl["assembly"]["chromosomes"])
        
        return acc_count