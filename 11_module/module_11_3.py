import inspect
import sys

def introspection_info(object):
    result = {'type': type(object), 'attributes': [], 'methods': [], 'module': inspect.getmodule(object)}
    for obj in dir(object):
        if callable(getattr(object, obj)):
            result['methods'].append(obj)
        else:
            result['attributes'].append(obj)
    return result

info = introspection_info('Слово')
print(info)





