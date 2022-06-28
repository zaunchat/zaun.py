import os
import glob
import importlib

def get_actions():
    middlewares = {}
    
    for path in glob.glob(
        os.path.join(os.path.dirname(__file__), '*.py')):
        
        if path.endswith('__init__.py'):
            continue
        
        mod = importlib.import_module(
            'itchat' + '.' + 'client' + '.' + 'actions' + '.' + os.path.basename(path)[:-3],
        )
        
        if hasattr(mod, 'export'):
            middlewares[mod.export()[0]] = mod.export()[1]
            
    return middlewares