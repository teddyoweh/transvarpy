 

class Lists:
 
    def __init__(self,items):
        self.items:dict = items
        for i in self.items:
            self.globals = globals()[i]= items[i]
            print(teddy)
     
 
    def add_prefix_all(self,prefix):
         for p in self.items:
            pref = f'{p}{prefix}'
            self.globals = globals()[pref]= self.items[p]
    def add_suffix_all(self,suffix):
        for s in self.items:
            suff = f'{suffix}{s}'
            self.globals = globals()[suff]= self.items[s]
            print(suff)
    def add_prefix(self,prefix,index):
               pass  
        
        
   
  

item =Lists(
    {'teddy':'oweh'
     ,'keka':'dindu'}
    )
item.add_prefix_all('names_')
item.add_suffix_all('names_')
 
