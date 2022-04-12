def filetodict(filename):
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
        
        return box

filetodict('SETU')