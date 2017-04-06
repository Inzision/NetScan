import dpkt
import socket
import datetime

f = open("mycap.pcap")
pcap = dpkt.pca.Reader(f)
for ts, buf in pcap:
	try:
		eth = dpkt.ethernet.Ethernet(buf)
		ip = eth.data
		src = socket.inet_ntoa(ip.src)
		dst = socket.inet_ntoa(ip.dst)
		if ip.p == dpkt.ip.IP_PROTO_TCP:
			tcp = ip.data
			print ("TCP PACKET")
			print ("Source Port: %s \tDestination Port: %s" %(tcp.sport,tcp.dsport))
		elif ip.p == dpkt.ip.IP_PROTO_UDP:
			udp = ip.data
			print ("UDP PACKET")
			print ("Source Port: %s \tDestination Port: %s" %(udp.sport,udp.dsport))
		else:
			pass
		print ("Source IP: %s \tDestination IP: %s" %(src,dst))
		print ("Source MAC: %s \tDestination MAC: %s" %(eth.src,eth.dst))
		print ("Time: %s" %(str(datetime.datetime.utcfromtimestamp(ts))))
		print ("")
	except:
		pass
f.close()
