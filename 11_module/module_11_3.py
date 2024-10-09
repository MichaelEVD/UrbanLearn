import inspect
import sys
from pprint import pprint

def introspection_info(atribut):
    info = []
    info.append(type(atribut))
    info.append(callable(atribut))
    info.append(isinstance(atribut,int))
    info.append(sys.path)
    info.append(inspect.getmodule(introspection_info))
    info.append(dir(atribut))
    return info

obj = 'Слово'
odj_info = introspection_info(obj)

for i in odj_info:
    pprint(i)





