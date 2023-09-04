import argparse
import shutil
import os
from plugin import find_required_plugin
from check import check_uninstall
import sys

def run():
    try:
        args = sys.argv[1:] 
        for arg in args:
            if os.path.isdir('plugins/'+arg):
                required_modules = find_required_plugin('plugins/'+arg)
                if required_modules != '':
                    check_uninstall(set(required_modules.split(",")))
                shutil.rmtree(os.path.normpath('plugins/'+arg))
    except Exception as e:
        print(e)