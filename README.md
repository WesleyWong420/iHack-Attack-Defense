# iHack Attack & Defense CTF
Please study and prepare :(

## Overview
- [How the Defcon Attack/Defense CTF 2018 Worked - LiveOverFlow](https://www.youtube.com/watch?v=RkaLyji9pNs)
- [HackTheBox - CyberMayhem](https://www.youtube.com/watch?v=XPyp_RP7OMY&list=WL&index=3&t=19s)
- **IMPORTANT:** [Defcamp finals 2022: Feedback on our first Attack/Defense CTF](https://www.riskinsight-wavestone.com/en/2022/11/defcamp-finals-2022-feedback-on-our-first-attack-defense-ctf/)

## Network Monitor & Detection
### Tools
- **IMPORTANT:** [Caronte](https://github.com/eciavatta/caronte)
- [Cardinal](https://github.com/vidar-team/Cardinal)

### Strategy
- **IMPORTANT:** Capture PCAP and Replay Attack (TCPDump + Tshark)
- Parse event logs & `access.log` file
- Check established connection `netstat` & kill enemy shell

## Attacking
### Exploit Runner
- [CSE 545 F18: 4-16-18 "Attack-Defense CTF Prep](https://github.com/AchyuthaBharadwaj/PCTF)
- **IMPORTANT:** [CISCO SECCON AD-CTF 2020](https://medium.com/csictf/cisco-seccon-2020-ad-ctf-2614b27f387a)

### Strategy
- Plant Persistence Backdoor 

### References
- [HackTricks](https://book.hacktricks.xyz/welcome/readme)
- [Pentest Everything](https://viperone.gitbook.io/pentest-everything/)
- [Pentester's Promiscuous Notebook](https://ppn.snovvcrash.rocks/)

## Patching
### Tools
- [Linux Smart Enumeration](https://github.com/diego-treitos/linux-smart-enumeration)
- [Joern](https://github.com/joernio/joern) [[Demo](https://www.youtube.com/watch?v=qtGRNb_2Khs)]
- [Snyk](https://github.com/snyk/) [[Demo](https://www.youtube.com/watch?v=tyL3Ouais1c)]

### Strategy
- Find misconfiguration on Linux Host using LSE
- Source Code Review
- Least Privilege (Access Control)
- Firewall Rule
- Change Default Passwords
- Remove Backdoor (Hidden Files `.shell.php`)

### References
- [ChatGPT](https://chat.openai.com/chat)
- [Vulnerable Code Snippets 1](https://github.com/snoopysecurity/Vulnerable-Code-Snippets)
- [Vulnerable Code Snippets 2](https://github.com/yeswehack/vulnerable-code-snippets)
- [Vuln Service Example](https://github.com/oldeurope/rwthctf2012/tree/master/services)
