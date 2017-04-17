import sys
from scapy import*

pkt=None

def usage():
  if len(sys.argv) != 2:
    print "Usage:", sys.argv[0], "10.10.111.110"
    
def crafted(character):
  global pkt
  global dest
  dest="10.10.111.107"
  char = ord(character)
  pkt = IP(dst=dest)/TCP(sport=char, dport=RandNum(0, 65535), flags="E")
  return pkt
  
def client():
  while true:
    message = raw_input('Enter your message: ')
    message += "\n"
    print "Sending data: " + message
    for char in message:
      new_pkt = crafted(char)
      send(new_pkt)
      
usage()
client()