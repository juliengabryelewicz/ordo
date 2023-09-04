import pkg_resources
import subprocess
import os
import sys

def check_install(required):
    installed = {pkg.key for pkg in pkg_resources.working_set}
    missing = required - installed

    if missing:
        subprocess.check_call(['poetry', 'run', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)

def check_uninstall(modules):
    subprocess.check_call(['poetry', 'run', 'pip', 'uninstall', '-y', *modules], stdout=subprocess.DEVNULL)