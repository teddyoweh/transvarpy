from types import FunctionType
from copy import copy

def copy_function(fn):
    return FunctionType(copy(fn.func_code), copy(fn.func_globals), name=item,
                        argdefs=copy(fn.func_defaults),
                        closure=copy(fn.func_closure))

list = ['one', 'two', 'three']

for item in list:
    def _fn():
        print(item)
    globals()[item] = copy_function(_fn)
list = map(eval, list)