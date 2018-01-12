from os import path
import os
import re
from copy import copy

def write_output_to_file(function):
    def inner_func(*args, **kwargs):
        root = os.path.abspath(os.path.curdir)
        _path = path.join(root, "RESP_{additional_info}".format(additional_info=function.__name__ + ".txt"))
        with open(_path, 'a+') as f:
            result = function(*args, **kwargs)
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
    return inner_func

def remove_all_symbols(string):
    _str = copy(string)
    _exclude = ['\n']
    for i in _exclude:
        try:
            _str = re.sub(i, '', _str)
        except Exception:
            pass
    return _str

def remove_if_exist(file_path):
    try:
        os.remove(file_path)
    except Exception as e:
        print(e)


