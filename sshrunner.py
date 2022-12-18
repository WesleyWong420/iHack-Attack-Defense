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

]

def do_submit(folderpath):
    files = os.listdir(folderpath)
    for file in files:
        if file.endswith('.sh') and file not in ignored_files:
            print(colored(f'[INFO][{datetime.now()}] Carving flags via SSH persistence using {file}!', 'blue', attrs=["bold"]))
            os.system(f'sh {os.path.join(folderpath, file)} | tee loot.txt')

            if os.path.exists('loot.txt'):
                fp = open('loot.txt', "r")
                output = fp.read()
                fp.close()
                os.remove('loot.txt')
                flags = extract_flag(output)

            for flag in flags:
                print(colored(f'    [FLAG] {flag}', 'green', attrs=["bold"]))

            # submit_flag(flags)

print(colored(f'[INFO][{datetime.now()}] Folder path set to {folderpath}', 'blue', attrs=["bold"]))

i = 0
while True:
    print(colored(f'[INFO][{datetime.now()}] Submitting for tick {i}', 'blue', attrs=["bold"]))
    do_submit(folderpath)

    i += 1
    print(colored(f'[SLEEP] Sleeping...', 'yellow', attrs=["bold", "blink"]))
    time.sleep(tickinterval)
    print('\n')
