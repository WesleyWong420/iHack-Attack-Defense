from pwn import remote
from termcolor import colored
import re

def extract_flag(text):
    return re.findall(r'1CJ2018\{\w{4}\}', text)

def submit_flag(flag, host='10.40.0.2', port=5555):
    if isinstance(flag, list):
        flag = '\n'.join(flag)

    print(colored(f'[INFO] Submitting flag {flag} to {host}:{port}.', 'green', attrs=["bold"]))

    r = remote(host, port)
    r.sendline(flag)
    
    if '\n' in flag:
        for _ in range(len(flag.split('\n'))):
            print(r.recvline())
    else:
        print(r.recvline())

    r.close()
