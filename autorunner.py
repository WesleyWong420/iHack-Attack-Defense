#!/usr/bin/python3

from datetime import datetime
from termcolor import colored
from utilities import extract_flag, submit_flag
import time
import sys
import os
from subprocess import call

folderpath = sys.argv[1]
tickinterval = 5 * 60 

ignored_files = [
    '__init__.py',
    'utilities.py',
    'autorunner.py'
]

def do_submit(folderpath):
    files = os.listdir(folderpath)
    for file in files:
        if file.endswith('.py') and file not in ignored_files:
            print(colored(f'[INFO][{datetime.now()}] Executing exploit in {file}!', 'blue', attrs=["bold"]))
            os.system(f'python3 {os.path.join(folderpath, file)}')

print(colored(f'[INFO][{datetime.now()}] Folder path set to {folderpath}', 'blue', attrs=["bold"]))

i = 0
while True:
    print(colored(f'[INFO][{datetime.now()}] Submitting for tick {i}', 'blue', attrs=["bold"]))
    do_submit(folderpath)

    i += 1
    print(colored(f'[SLEEP] Sleeping...', 'yellow', attrs=["bold", "blink"]))
    time.sleep(tickinterval)
    print('\n')
