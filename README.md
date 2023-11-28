# iHack 2022 Attack & Defense CTF

## Overview
- **USEFUL**: [HackTheBox - CyberMayhem by Ippsec](https://www.youtube.com/watch?v=o42dgCOBkRk)
- **IMPORTANT:** [Defcamp finals 2022: Feedback on our first Attack/Defense CTF](https://www.riskinsight-wavestone.com/en/2022/11/defcamp-finals-2022-feedback-on-our-first-attack-defense-ctf/)
- **VERY IMPORTANT:** [CISCO SECCON AD-CTF 2020](https://medium.com/csictf/cisco-seccon-2020-ad-ctf-2614b27f387a)
- **VERY IMPORTANT:** [Pre-CTF Training Session - Day 1](https://www.youtube.com/live/u9ypv7wY9o0?si=Of-mLvgRzxOFcF_4)
- **VERY IMPORTANT:** [Pre-CTF Training Session - Day 2](https://www.youtube.com/live/sGk4trFj5sU?si=z2uYG1GryBoT-cm2)
  
## Vuln Services
- [CJ2018 CTF](https://github.com/farisv/CJ2018-Final-CTF) [[Solution](https://rhamaa.github.io/post/2018/10/17/Cyber-Jawara-2018-Final-Web-Exploitation/)]
- [ICC2022-AD-CTF](https://github.com/CybersecNatLab/ICC2022-AD-CTF)
- [HITB SECCCONF EDU CTF 2021](https://github.com/HITB-CyberWeek/hitbsecconf-ctf-2021)
- [HITB SECCONF CTF 2022](https://github.com/HITB-CyberWeek/hitbsecconf-ctf-2022)
- [HITB SECCONF CTF 2023](https://github.com/HITB-CyberWeek/hitbsecconf-ctf-2023)

## Attacking
### Tools
- [S4DFarm](https://github.com/C4T-BuT-S4D/S4DFarm)

## Network Monitor & Detection
### Tools
- [Caronte](https://github.com/eciavatta/caronte) [[Documentation](https://app.swaggerhub.com/apis-docs/eciavatta/caronte/WIP#/)]
- [Tulip](https://github.com/OpenAttackDefenseTools/tulip)

### Strategy
- Incident Response
  - `w`
  - `ps -aef --forest`
  - `ss -anp {PID}`   
  - `kill -9 {PID}`
  - `cd /proc/{PID}; ls -al | grep cwd`
  - `tail /var/log/apache2/access.log`
  - `nohup tcpdump -i eth0 -w tcpdump.cap -s 0 &`

## Patching
### Strategy
- Rollout Patched Services
  - `sudo docker-compose down`
  - `sudo docker-compose build`
  - `docker-compose up --force-recreate -d`
