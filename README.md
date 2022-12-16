# iHack Attack & Defense CTF
Please study and prepare :(

## Overview
- [How the Defcon Attack/Defense CTF 2018 Worked - LiveOverFlow](https://www.youtube.com/watch?v=RkaLyji9pNs)
- **USEFUL**: [HackTheBox - CyberMayhem by Ippsec](https://www.youtube.com/watch?v=o42dgCOBkRk)
- **IMPORTANT:** [Defcamp finals 2022: Feedback on our first Attack/Defense CTF](https://www.riskinsight-wavestone.com/en/2022/11/defcamp-finals-2022-feedback-on-our-first-attack-defense-ctf/)
- **VERY IMPORTANT:** [CISCO SECCON AD-CTF 2020](https://medium.com/csictf/cisco-seccon-2020-ad-ctf-2614b27f387a)

## Vuln Services
- [CJ2018 CTF](https://github.com/farisv/CJ2018-Final-CTF) [[Solution](https://rhamaa.github.io/post/2018/10/17/Cyber-Jawara-2018-Final-Web-Exploitation/)]
- [Vuln Service Example](https://github.com/oldeurope/rwthctf2012/tree/master/services)

## Network Monitor & Detection
### Tools
- [Caronte](https://github.com/eciavatta/caronte) [[Documentation](https://app.swaggerhub.com/apis-docs/eciavatta/caronte/WIP#/)]
- [Packmate](https://gitlab.com/packmate/Packmate/-/blob/master/README_EN.md)
- [Tulip](https://github.com/OpenAttackDefenseTools/tulip)

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
  - `nohup tcpdump -i tun0 -w tcpdump.cap -s 0 &`

## Attacking
### Exploit Runner
- [CSE 545 F18: 4-16-18 "Attack-Defense CTF Prep](https://github.com/AchyuthaBharadwaj/PCTF)

### Strategy
- Rust Scan > Nmap
- SSH Backdoor [[persistence.sh](persistence.sh)]
- Use meterpreter whenever possible
- Check bash history

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
- SECCOMP [[Demo](https://attackdefense.com/challengedetailsnoauth?cid=1826)]
- Hardening
  - Disable unsafe functions like `shell_exec` in `php.ini` config file

### References
- [ChatGPT](https://chat.openai.com/chat)
- [Vulnerable Code Snippets 1](https://github.com/snoopysecurity/Vulnerable-Code-Snippets)
- [Vulnerable Code Snippets 2](https://github.com/yeswehack/vulnerable-code-snippets)
