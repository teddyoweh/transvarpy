from transvar import transdict
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
    def _(self,_globals):
        return(_globals.update(globals()))
    def init(self):
        self.newd = transdict(self.box)
    def init_prefix(self,prefix):
        self.newd.add_prefix_all(prefix)
    def init_suffix(self,suffix):
        self.newd.add_suffix_all(suffix)
    def print_var(self):
        print(f' {len(self.box)} Variables Created: ')
        for num,los in enumerate(self.box):
           
            statement = '[{}] {}={}'.format(num,los,self.box[los])
            print(statement)
 
