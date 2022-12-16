while true; 
do 
  sudo tcpdump -i eth0 -w tcpdump.pcap &
  sleep 3
  _pid=$! 
  sleep 60
  kill -9 $_pid
  sleep 3
  curl -F "file=@tcpdump.pcap" "http://localhost:3333/api/pcap/upload"
  sudo rm tcpdump.pcap
done
