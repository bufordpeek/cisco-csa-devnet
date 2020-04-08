#!/usr/bin/python3

# General imports
import os
import sys
import traceback
import getopt

# importing ipaddress
import re

def Main(args):
	try:
		continueLoop = True 

		while(continueLoop):
			#Getting IP address
			ipAddr 	= input("Enter IP Address (Type x to End):")
			
			#cleaning white space
			ipAddress = ipAddr.rstrip()

			if ( ipAddress.upper() == 'X' ):
				continueLoop = False
			elif ( validateIpAddress(ipAddress) ):
				print(ipAddress + " is a Valid IP Address! ")
			else:
				print(ipAddress + " is not valid IP Address! ")
	
		return(0)	

	except Exception as X:
		print(X)
		raise(traceback.format_exc())
		

	finally:
		print("Cisco Systems, Inc (c) (2020)")

def validateIpAddress(ip="127.0.0.1"):
	isIP = re.match(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", ip)
	
	if(isIP is None):
		return(False)
	else:
		octets = ip.split(".")
		for octet in octets:
			if ( int(octet) > 255 or int(octet) < 0 ):
				return(False)

	return(True)


# Usage
def usage():
	print (sys.argv[0])

if ( __name__ == '__main__' ):
	sys.exit(Main(sys.argv[1:]))
