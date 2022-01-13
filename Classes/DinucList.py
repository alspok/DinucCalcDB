class DinucList():
    
    def __init__(self):
        self.nuc = ['a', 'c', 'g', 't']
    
    def dinucInit(self) -> list:
        return [nuc1 + nuc2
                for nuc1 in self.nuc
                for nuc2 in self.nuc
               ]
    
    def trinucInit(self) -> list:
        return[nuc1 + nuc2 + nuc3
               for nuc1 in self.nuc
               for nuc2 in self.nuc
               for nuc3 in self.nuc
              ]