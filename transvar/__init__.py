
# -*- coding=utf-8 -*-
# Name: teddy oweh
# Email: teddy@teddyoweh.net
# Message: Feel Free To Contact Me on Enquires or Question, il Reply :)
from transvar import transdict
from transvar import transfile
from transvar import transindv

class transdict:
 
    def __init__(self,items):
        """
        Args:
            items (dict): A dictionary containing variable names as the keys and the target value of the variables as the values.
        """
        self.items:dict = items
        for i in self.items:
            self.globals = globals()[i]= items[i]
    def init(self,_globals):
        """
        `transdict.init(globals())\n
        Parse the globals function
        
      
        """
        return(_globals.update(globals()))
    def getdictval_value(self,string:str):
      
        return [t for x, t in enumerate(self.items) if t==string][0]
    def getdictval_index(self,index:int):
       
        return [t for x, t in enumerate(self.items) if x==int(index)][0]
    def add_prefix_all(self,prefix_a):
        for p in self.items:
            pref = f'{prefix_a}{p}'
            self.globals = globals()[pref]= self.items[p]
        """
         Add a prefix to all the variables that has been created.
        Args:
            prefix_a (str): A string to add as a prefix to all the variables created.
        """
    def add_suffix_all(self,suffix_a):
        """
         Add a suffix to all the variables that has been created.
        Args:
            suffix_a (str): A string to add as a prefix to all the variables created.
        """
        for s in self.items:
            suff = f'{s}{suffix_a}'
            self.varname = suff
            
            self.globals = globals()[suff]= self.items[s]
        
          
    def add_prefix(self,prefix=None,index:int=None,value:str=None):
        """
         Add a prefix to a specific variable that has been created.
         
        `add_prefix(prefix='_1' index='0' )`
        ## or 
        `add_prefix(prefix='_1' value='dict_key' )`
        """
    
        if value is None:
            self.globals = globals()[f'{prefix}{self.getdictval_index(index)}']= self.items[self.getdictval_index(index)]
        if index is None:
            self.globals = globals()[f'{prefix}{self.getdictval_value(value)}']= self.items[self.getdictval_value(value)]
            
            
    def add_suffix(self,suffix=None,index:int=None,value:str=None):
        """
        
         Add a suffix to the current variable that has been created using either the index or the value to identify which a prefix should be added to.
        
        `add_suffix(suffix='_1' index='0')`
        ## or 
        `add_suffix(suffix='_1' value='dict_key') 
        """
        if value is None:
            self.globals = globals()[f'{self.getdictval_index(index)}{suffix}']= self.items[self.getdictval_index(index)]
        if index is None:
            self.globals = globals()[f'{self.getdictval_value(value)}{suffix}']= self.items[self.getdictval_value(value)]
            
            
        
class transindv:       
    def __init__(self,var,value):
        """
        Args: (var,value)
        var: Name of the variable to be create
        value: Value to be assigned to the variable that has been created.
        """
        item = var
        self.item = item
        
        self.globals = globals()[item]= value
        
    def init(self,_globals):
        return(_globals.update(globals())) 
    def getdictval_value(self,string:str):
      
        return [t for x, t in enumerate(self.items) if t==string][0]
    def getdictval_index(self,index:int):
       
        return [t for x, t in enumerate(self.items) if x==int(index)][0]
    def add_prefix(self,prefix_a):
        """
         Add a prefix to the variable that has been created.
        Args:
            prefix_a (str): A string to add as a prefix to all the variables created.
        """
        pref = f'{self.item}{prefix_a}'
        self.globals = globals()[pref]= self.item
    def add_suffix(self,suffix_a):
        """
         Add a suffix to the variable that has been created.
        Args:
            suffix_a (str): A string to add as a suffix to all the variables created.
        """
        suff = f'{suffix_a}{self.item}'
        self.varname = suff
        self.globals = globals()[suff]= self.items
        

class transfile:
    
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
    def __merge(self,_globals):
        return(_globals.update(globals()))
    def init(self,_globals):
        self.newd = transdict(self.box)
        self.__merge(_globals)
    def prefix(self,prefix):
        self.newd.add_prefix_all(prefix)
    def suffix(self,suffix):
        self.newd.add_suffix_all(suffix)
    def print_vars(self):
        print(f' {len(self.box)} Variables Created: ')
        for num,los in enumerate(self.box):
           
            statement = '[{}] {}={}'.format(num,los,self.box[los])
            print(statement)
 



 
 
