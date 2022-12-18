# iHack Attack & Defense CTF
Please study and prepare :(

## Overview
- [How the Defcon Attack/Defense CTF 2018 Worked - LiveOverFlow](https://www.youtube.com/watch?v=RkaLyji9pNs)
- **USEFUL**: [HackTheBox - CyberMayhem by Ippsec](https://www.youtube.com/watch?v=o42dgCOBkRk)
- **IMPORTANT:** [Defcamp finals 2022: Feedback on our first Attack/Defense CTF](https://www.riskinsight-wavestone.com/en/2022/11/defcamp-finals-2022-feedback-on-our-first-attack-defense-ctf/)
- **VERY IMPORTANT:** [CISCO SECCON AD-CTF 2020](https://medium.com/csictf/cisco-seccon-2020-ad-ctf-2614b27f387a)

## Vuln Services
- [CJ2018 CTF](https://github.com/farisv/CJ2018-Final-CTF) [[Solution](https://rhamaa.github.io/post/2018/10/17/Cyber-Jawara-2018-Final-Web-Exploitation/)]

## Network Monitor & Detection
### Tools
- [Caronte](https://github.com/eciavatta/caronte) [[Documentation](https://app.swaggerhub.com/apis-docs/eciavatta/caronte/WIP#/)]

### Strategy

- Remove Backdoor
  - Hidden Files `.shell.php`
  - SSH Keys
  - Cronjobs
  - User Accounts
- Incident Response
  - `w`
  - `ps -aef --forest`
  - `ss -anp {PID}`   
  - `kill -9 {PID}`
  - `cd /proc/{PID}; ls -al | grep cwd`
  - `tail /var/log/apache2/access.log`
  - `nohup tcpdump -i eth0 -w tcpdump.cap -s 0 &`

## Attacking

### Strategy
- Rustscan > Nmap > Dir-busting > Subdomain-busting
- Use meterpreter whenever possible
- Meterpreter scripts & Nmap scripts enumeration
- Burp URL encoding
- Crackmapexec for brute forcing SSH, FTP, SMB
- Upload shell to FTP/SSH, and LFI to execute
- Anon login FTP, MySQL
- SQLMap (--os-shell)
- LFI, IDOR, XXE, 
- Check bash history
- Grep recursive for passwords `grep -R -i "pass" *`
- sudo -l, suid, cronjobs
- Linpeas
- Lateral Movement - Hidden Services
- SSH backdoor

### References
- [HackTricks](https://book.hacktricks.xyz/welcome/readme)
- [Pentest Everything](https://viperone.gitbook.io/pentest-everything/)
- [Pentester's Promiscuous Notebook](https://ppn.snovvcrash.rocks/)
- [Linux Persistence Technique](https://www.linode.com/docs/guides/linux-red-team-persistence-techniques/)
- [Pentest Checklist](https://systemweakness.com/basic-pentesting-cheat-sheet-c43e1647c753)

## Patching
> Remember to backup before patching!

### Strategy
- Find misconfiguration on Linux Host using LinuxSmartEnumeration & LinPEAS
- Source Code Review
- Least Privilege (Access Control)
- Change Default Passwords
- Firewall Rule
- Hardening
  - Disable unsafe functions like `shell_exec` in `php.ini` config file

### References
- [ChatGPT](https://chat.openai.com/chat)
- [Vulnerable Code Snippets 1](https://github.com/snoopysecurity/Vulnerable-Code-Snippets)
- [Vulnerable Code Snippets 2](https://github.com/yeswehack/vulnerable-code-snippets)
