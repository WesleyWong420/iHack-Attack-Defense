while true; 
do 
  sudo tcpdump -i eth0 -w tcpdump.pcap &
  sleep 3
  _pid=$! 
  sleep 60
  kill -9 $_pid
  sleep 3
  data=`cat tcpdump.pcap`
  curl -i -s -k -X $'POST' \
      -H $'Host: localhost:3333' -H $'Accept: */*' -H $'Content-Type: multipart/form-data; boundary=---------------------------40903555511780393260267180294' -H $'Authorization: Basic cGlrYXJvb3Q6cGlrYXJvb3Q=' \
      --data-binary $'\x0d\x0a-----------------------------40903555511780393260267180294\x0d\x0aContent-Disposition: form-data; name=\"file\"; filename=\"tcpdump.pcap\"\x0d\x0aContent-Type: application/vnd.tcpdump.pcap\x0d\x0a\x0d\x0a$data\x0d\x0a-----------------------------40903555511780393260267180294\x0d\x0aContent-Disposition: form-data; name=\"flush_all\"\x0d\x0a\x0d\x0afalse\x0d\x0a-----------------------------40903555511780393260267180294--\x0d\x0a' \
      $'http://localhost:3333/api/pcap/upload'
  sudo rm tcpdump.pcap
done
