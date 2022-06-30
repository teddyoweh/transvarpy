class TransIndv:       
    def __init__(self,item,value):
        """ app"""
        self.item = item
        
        self.globals = globals()[item]= value
        
    def _(self,_globals):
        return(_globals.update(globals())) 
    def getdictval_value(self,string:str):
      
        return [t for x, t in enumerate(self.items) if t==string][0]
    def getdictval_index(self,index:int):
       
        return [t for x, t in enumerate(self.items) if x==int(index)][0]
    def add_prefix(self,prefix_a):
         
        pref = f'{self.item}{prefix_a}'
        self.globals = globals()[pref]= self.item
    def add_suffix(self,suffix_a):
      
        suff = f'{suffix_a}{self.item}'
        self.varname = suff
        self.globals = globals()[suff]= self.items