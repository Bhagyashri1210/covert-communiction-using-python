import sys
from scapy.all import*

def parse(pkt):
  flag = pkt['TCP'].flags
  if flag == 0X40:
    char = chr(pkt['TCP'].sport)
    sys.stdout.write(char)
    
sniff(filter="tcp",prn=parse)