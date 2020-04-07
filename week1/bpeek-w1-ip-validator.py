#!/usr/bin/python3

# General imports
import os
import sys
import traceback
import getopt

# importing ipaddress
import ipaddress
import re

def Main(args):
	try:
		continueLoop = True 

		while(continueLoop):
			#Getting IP address
			ipAddr 	= input("Enter IP Address (Type x to End):")
			
			#cleaning white space
			ipAddress = ipAddr.rstrip()

			if ( ipAddress.capitalize() == 'X' ):
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
	try:
		ip_addr = ipaddress.ip_address(ip)
	except Exception:
		return False

	return(True)


# Usage
def usage():
	print (sys.argv[0])

if ( __name__ == '__main__' ):
	sys.exit(Main(sys.argv[1:]))
