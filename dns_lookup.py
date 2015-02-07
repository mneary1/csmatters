import re, socket 

while True:
	name = str(input("Enter a host name or ip address (q to quit): "))
	
	#regex to match ip adress 
	ip = re.compile("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
	
	if 'q' in name or 'Q' in name: 
		break
	
	if ip.match(name):
		try:
			print(socket.gethostbyaddr(name)[0])
		except:
			print("Failed to lookup the host name of " + name + " :(")
	else:
		try:
			print(socket.gethostbyname(name))
		except:
			print("Failed to lookup the IP address of " + name + " :(")	
