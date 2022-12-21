from pwn import remote
from termcolor import colored
from datetime import datetime
import re
import requests
import sys
import os

def extract_flag(text):
    return re.findall(r'ihack\{\w{21}\}', text)

def submit_flag(flag):

    cmd = "curl --location --request POST 'https://10.10.10.10/api/exercises/54ba9539-03a5-4441-9fb1-c85409f9ee0d/ctfad-submissions' --header 'Accept: application/json' --header 'Content-Type: application/json' --header 'Authorization: Bearer {19|ECXrUMhrzwhDy7GWvgWbmZyv7Vo4iLb636apq4I1}'--data-raw '{\"flags\": [" + flag + "]}'"

    os.system(f'{cmd}')

    print(colored(f'[INFO][{datetime.now()}] Submitting flag {flag}', 'green', attrs=["bold"]))
