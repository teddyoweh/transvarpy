class transdict:
     
    def __init__(self,items):
        self.items:dict = items
        for i in self.items:
            self.globals = globals()[i]= items[i]
    def init(self,_globals):
        """
        `transdict.init(globals())\n
        Parse the globals function\
        
      
        """
        return(_globals.update(globals()))
    def __getdictval_value(self,string:str):
      
        return [t for x, t in enumerate(self.items) if t==string][0]
    def __getdictval_index(self,index:int):
       
        return [t for x, t in enumerate(self.items) if x==int(index)][0]
    def add_prefix_all(self,prefix_a):
        """
         Add a prefix to all the variables that has been created.
        
        """
        for p in self.items:
            pref = f'{prefix_a}{p}'
            self.globals = globals()[pref]= self.items[p]
        
    def add_suffix_all(self,suffix_a):
        """
         Add a suffix to all the variables that has been created.
        
        """
        for s in self.items:
            suff = f'{s}{suffix_a}'
            self.varname = suff
            
            self.globals = globals()[suff]= self.items[s]
        
          
    def add_prefix(self,prefix=None,index:int=None,value:str=None):
        """
         Add a prefix to a specific variable that has been created.
        
        """
    
        if value is None:
            self.globals = globals()[f'{prefix}{self.getdictval_index(index)}']= self.items[self.getdictval_index(index)]
        if index is None:
            self.globals = globals()[f'{prefix}{self.getdictval_value(value)}']= self.items[self.getdictval_value(value)]
            
            
    def add_suffix(self,suffix=None,index:int=None,value:str=None):
        """
         Add a suffix to the current variable that has been created using either the index or the value to identify which a prefix should be added to.`
         
         add_suffix(
             suffix='_1'
             index='0' 
         )
        
        """
        if value is None:
            self.globals = globals()[f'{self.getdictval_index(index)}{suffix}']= self.items[self.getdictval_index(index)]
        if index is None:
            self.globals = globals()[f'{self.getdictval_value(value)}{suffix}']= self.items[self.getdictval_value(value)]
            