 

class TransDict:
 
    def __init__(self,items):
        self.items:dict = items
        for i in self.items:
            self.globals = globals()[i]= items[i]
            
    def getdictval_value(self,string:str):
      
        return [t for x, t in enumerate(self.items) if t==string][0]
    def getdictval_index(self,index:int):
       
        return [t for x, t in enumerate(self.items) if x==int(index)][0]
    def add_prefix_all(self,prefix_a):
        for p in self.items:
            pref = f'{prefix_a}{p}'
            self.globals = globals()[pref]= self.items[p]
        
    def add_suffix_all(self,suffix_a):
        for s in self.items:
            suff = f'{s}{suffix_a}'
            self.varname = suff
            
            self.globals = globals()[suff]= self.items[s]
        
          
    def add_prefix(self,prefix=None,index:int=None,value:str=None):
        """
         Add a prefix to the current variable that has been created
        
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
            
            
        
class TransIndv:       
    def __init__(self,item,value):
        """ app"""
        self.item = item
        
        self.globals = globals()[item]= value
        
      
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
        

class TransFile:
    
    def __init__(self,filename):
        try:
            file = open(filename,'r')
        except FileNotFoundError:
            print("{} is not in directory".format(filename))
        else:
            files = file.readlines()
            box  = {}
            for i in files:
                i = i.strip('\n')
                nam = i.split('=')
                
                for i in range(50):
                    space = ' '*i
                    nam[0]=nam[0].replace(space,'')
                    nam[1]=nam[1].replace(space,'')
                box[nam[0]] =nam[1]
            
            self.box = box

    def init(self):
        self.newd = TransDict(self.box)
    def init_prefix(self,prefix):
        self.newd.add_prefix_all(prefix)
    def init_suffix(self,suffix):
        self.newd.add_suffix_all(suffix)
    def print_var(self):
        print(f' {len(self.box)} Variables Created: ')
        for num,los in enumerate(self.box):
           
            statement = '[{}] {}={}'.format(num,los,self.box[los])
            print(statement)
 



TransIndv('*','teddy')
print(globals())