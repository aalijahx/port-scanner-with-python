# PORT SCANNER IN PYTHON
# It takes ip address from the user in command line and finds the ports open on that ip address


#importing 'sys', 'socket' and 'datetime' module
import sys
import socket
from datetime import datetime

# in command line if arguments given are less than two it will give error message because we need 2 arguments to run this program
# first would be 'argument 0' which would be the name of our file, second would be 'argument 1' which would be the target ip address
# correct syntax should be: python3 filename.py(argument 0) 192.168.0.0(argument 1)
if len(sys.argv) != 2:
	print("invalid number of arguments.\nCorrect Syntax: python3 portscanner.py <ip address>")
	sys.exit()
else:
	target = socket.gethostbyname(sys.argv[1])

#banner of our port scanner tool
print("-" * 50)
print(f"target: {target}")
print(f"Time started: {datetime.now()}")
print("-" * 50)
try:
# currently it will scan ports from 50 to 84 - you can change it for scanning different ports accordingly
	for port in range(50,85):
		s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		socket.setdefaulttimeout(1) # it will move on to next port after 1 second - you can also change that accordingly
		result = s.connect_ex((target,port)) # This would return 0 if connection is made(i.e. if port is open) and 1 if port is closed
		if result == 0:
			print(f"port {port} is open")
		s.close()

# here we have some of the possible exceptions that we could handle
except KeyboardInterrupt:
	print("program exiting")
	sys.exit()
except socket.gaierror:
	print("could not resolve host name")
	sys.exit()
except socket.error:
	print("could not connect!")
	sys.exit()
	
print("Scan Complete\nthanks for using our port scanner!")

