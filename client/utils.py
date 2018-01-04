from os import path
import os
import re
from copy import copy

def writeOutputToFile(function):
    def innerFunction(*args,**kwargs):
        root = os.path.abspath(os.path.curdir)
        _path = path.join(root, "RESP_{additional_info}".format(additional_info=function.__name__ + ".txt"))
        with open(_path,'a+') as f:
            result = function(*args,**kwargs)
            try:
                if isinstance(result, list):
                    for item in result:
                        if isinstance(item, dict):
                            for key, value in item.items():
                                f.write(key+","+value+'\n')
                        else:
                            f.write(item+'\n')

                else:
                    f.write(result)
            except Exception as e:
                f.write("Oh snap! ='( %s \n" % e)
    return innerFunction



def remove_all_symbols(string):
    _str = copy(string)
    _exclude = ['\n']
    for i in _exclude:
        try:
            _str = re.sub(i, '', _str)
        except Exception:
            pass
    return _str