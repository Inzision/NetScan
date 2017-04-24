from scapy.all import *
from dpkt.compat import compat_ord
import dpkt
import socket
import datetime

def mac_addr(address):#converts mac address from hex to a readable format
	return ':'.join('%02x' % compat_ord(b) for b in address)

packets = sniff(iface = "eth0",filter="tcp and port 80",count=50) #captures 50 tcp port 80 ports from interface specified
wrpcap("new.pcap",packets)#writes capture packets toa pcap file called new.pcap

f = open("new.pcap")
pcap = dpkt.pcap.Reader(f)

try:
	for ts, buf in pcap:
		eth = dpkt.ethernet.Ethernet(buf)#unpacks ethernet frame
		ip = eth.data# grabs data from ethernet frame(ip packet)
		src = socket.inet_ntoa(ip.src)#uses socket to grab source ip from ip packet
		dst = socket.inet_ntoa(ip.dst)#uses socket to grab destination ip from ip packet
		print ("Source IP: %s \tDestination IP: %s" %(src,dst))
		print ("Source MAC: %s \tDestination MAC: %s"%(mac_addr(eth.src),mac_addr(eth.dst)))#puts through funtion and prints out the mac addresses
		print ("")
		if ip.p == dpkt.ip.IP_PROTO_TCP:#checks to see if the ip packet is using TCP
			tcp = ip.data#grabs the data from the ip packet(TCP Fragment)and assigns it to tcp
			print ("TCP PACKET")
			print ("Source Port: %s \t\tDestination Port: %s" %(tcp.sport,tcp.dport))
		elif ip.p == dpkt.ip.IP_PROTO_UDP:#checks to see if the ip packet is using UDP
			udp = ip.data#grabs the data from the ip packet(UDP Fragment) and assigns it to udp
			print ("UDP PACKET")
			print ("Source Port: %s \t\tDestination Port: %s" %(udp.sport,udp.dport))
		else:
			pass
except:
	pass
f.close()
