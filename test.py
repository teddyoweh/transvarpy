def gettype(input):
    return str(type(input)).replace("<class '",'').replace("'>",'')


oo  = {'sd':4}
print(gettype(oo))


types  = ['str','list','dict','float','int','long']