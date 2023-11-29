import pandas as pd

class ClassIterator:
        """
        Передаём путь к файлу аннотации и label по которому мы ищем
        """
        
        def __init__(self, data_path: str, label: str):
            
            self.data = pd.read_csv(data_path)
            self.label = label
            self.index = 0


            while self.index < len(self.data):
                

                if str(self.data.iloc[self.index]["class"]) == self.label:

                
                    return None
                
                self.index += 1
                
            raise StopIteration
        
        
        def __iter__(self):


            return self
        

        def getRel(self) -> str:
            return self.data.iloc[self.index]["rel_path"]
        
        def getAbs(self) -> str:
            return self.data.iloc[self.index]["abs_path"]
        
        def getClass(self)-> str:
            return self.data.iloc[self.index]["class"]


        def __next__(self):
            
            self.index += 1
            
            while self.index < len(self.data):
                

                if str(self.data.iloc[self.index]["class"]) == self.label:

                
                    return self
                
                self.index += 1
                
            raise StopIteration
        
