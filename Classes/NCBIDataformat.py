import subprocess
import os

class NCBIDataformat():
    
    def ncbiDataformat(self, acc_list: list):
        for acc in acc_list:
                subprocess.run(".\\bin\\dataformat ")
        pass