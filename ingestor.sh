BLUE='\033[1;34m'
NC='\e[0m'
COUNTER=1

while true; 
do 
  now=$(date +"%T")
  sudo tcpdump -i eth0 -w tcpdump.pcap > /dev/null 2>&1 &
  echo "${BLUE}[INFO][${now}] Running TCPDump for tick ${COUNTER} ${NC}"
  sleep 1
  _pid=$! 
  sleep 60
  kill -9 $_pid
  sleep 3
  data=`cat tcpdump.pcap`
  python3 ingestor.py
  sudo rm tcpdump.pcap
  COUNTER=$((COUNTER+1))
done
