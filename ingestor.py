#!/usr/bin/python3

import requests

with open("tcpdump.pcap", mode="rb") as pcap_file:
	contents = pcap_file.read()

headers = {
    'Host': 'localhost:3333',
    'Accept': '*/*',
    'Content-Type': 'multipart/form-data; boundary=---------------------------40903555511780393260267180294',
    'Authorization': 'Basic cGlrYXJvb3Q6cGlrYXJvb3Q=',
}

data = bytes('\r\n-----------------------------40903555511780393260267180294\r\nContent-Disposition: form-data; name="file"; filename="tcpdump.pcap"\r\nContent-Type: application/vnd.tcpdump.pcap\r\n\r\n', 'utf-8') + contents + bytes('\r\n-----------------------------40903555511780393260267180294\r\nContent-Disposition: form-data; name="flush_all"\r\n\r\nfalse\r\n-----------------------------40903555511780393260267180294--\r\n', 'utf-8')

response = requests.post('http://localhost:3333/api/pcap/upload', headers=headers, data=data, verify=False)
print(response)
