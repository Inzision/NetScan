import socket

host = ""

def port_scan(host, port):
    try:
        s = socket(AF_INET, SOCK_STREAM, r_code = 1)
	    s.sockettimeout(0.01)#Might not need.
        connection = s.socket(host,port)
        if connection == 0:
            return_con = connection
        s.close()
    except Exception:
        pass
    return return_con

host = raw_input("Enter Target Host: ")
host_ip = host
min_port = input("Enter starting port: ")
max_port = input("Enter last port: ")
i = 0

for port in range(min_port, max_port+1):
    try:
        response = port_scan(host, port)
        if response == 0:
            print ("Port %d: Open" %(port))
            i += 1
    except Exception:
        pass

print i
print ("Scanning finished.")
        
