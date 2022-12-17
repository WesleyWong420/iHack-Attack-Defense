while true; 
do 
  sudo tcpdump -i eth0 -w tcpdump.pcap &
  sleep 3
  _pid=$! 
  sleep 30
  kill -9 $_pid
  sleep 3
  data=`cat tcpdump.pcap`
  python3 test.py
  sudo rm tcpdump.pcap
done
