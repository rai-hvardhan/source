import sys
It is a list of strings defining what symbols in a module will be exported when from <module> import * is used on the module.
def export(fn):
    mod = sys.modules[fn.__module__]
    if hasattr(mod, '__all__'):
        mod.__all__.append(fn.__name__)
    else:
        mod.__all__ = [fn.__name__]
    return fn

from platform import python_version()
print(python_version())
pip freeze
#PYTHONBREAKPOINT=0 disables debugging. Specifically, with this value sys.breakpointhook() returns None immediately.
SET environment variable PYTHONBREAKPOINT=0

	
import re
import pathlib
import os

p = pathlib.Path('.')

files = [str(y) for x in p.iterdir() if x.is_dir() and re.match(r'^[0-9]', str(x)) \
         for y in x.iterdir() if not y.is_dir() and re.match(r'^[0-9]', str(y))
        ]

def sortUdemyPath(aStr:str):
    folder, file = os.path.split(aStr)[-2:]
    matchFolder = re.search(r'^[0-9]+', folder)
    matchFile = re.search(r'^[0-9]+', file)
    if ( matchFolder is not None and matchFile is not None):
        return (int(matchFolder.group(0)), int(matchFile.group(0)))
        
                                 

files.sort(key=lambda x:sortUdemyPath(x))

with open('index.html', 'w') as f:
    for line in files:
        fullpath = os.path.join(os.getcwd(), line)
        folder, file = os.path.dirname(fullpath), os.path.basename(fullpath)
        os.rename(fullpath, os.path.join(folder, re.search(r'[0-9]+', file).group(0)) + pathlib.Path(file).suffix)
        #break	