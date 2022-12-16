for i in $(seq 128 129); 
do
  echo "192.168.231.$i"
  ssh -o "BatchMode=Yes" -o "StrictHostKeyChecking=no" -o "GlobalKnownHostsFile=/dev/null" -o "UserKnownHostsFile=/dev/null" root@192.168.231.$i "cat /home/kali/Desktop/flag.txt; echo; cat /home/kali/Desktop/flag.txt; echo" 2>/dev/null
done
