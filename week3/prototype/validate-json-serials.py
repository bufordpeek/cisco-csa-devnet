#!/usr/bin/python3

# 	Author: Buford Peek (<bupeek@cisco.com>)
#	Title:	Technical Solutions Architect
#

# General imports
import os
import sys
import traceback
import getopt

# Special imports
import json
import ipaddress

def Main(args):
	try:
		fd = open('./device-data.json')
		
		deviceData = json.load(fd)

		for device in deviceData:
			if (validateIpAddress(device['lanIp'])):
				print("[%s] is a valid IP for Device Serail [%s]" % (device['serial'], device['lanIp']))
			else:
				print("[%s] is NOT a valid IP for Device Serail [%s]" % (device['serial'], device['lanIp']))

		return(0)	

	except Exception as X:
		print(X)
		raise(traceback.format_exc())
		

	finally:
		print("Cisco Systems, Inc (c) (2020)")

# Validate IP Addresses
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
