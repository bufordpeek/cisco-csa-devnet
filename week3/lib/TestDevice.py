#!/usr/bin/python3


#
# Author: Buford Peek (bupeek@cisco.com)
#         Technical Solutions Architect


# python imports
import os
import sys
import json
import ipaddress

# updating the path
sys.path.append('.')


# Class Definition
class TestDevice(): 
	
	# default construstor
	def __init__(self, config=dict()):
		self.lat			= config['lat'] if ( 'lat' in config ) else ''
		self.lng			= config['lng'] if ( 'lng' in config ) else ''
		self.address		= config['address'] if( 'address' in config) else ''
		self.serial			= config['serial'] if( 'serial' in config) else ''
		self.lanIp			= config['lanIp'] if( 'lanIp' in config) else ''
		self.wan1Ip			= config['wan1Ip'] if( 'wan1Ip' in config) else ''
		self.wan2Ip			= config['wan2Ip'] if( 'wan2Ip' in config) else ''
		self.url			= config['url'] if( 'url' in config) else ''
		self.name			= config['name'] if( 'name' in config) else ''
		self.model			= config['model'] if( 'model' in config) else ''
		self.networkId		= config['networkId'] if( 'networkId' in config) else ''
		self.firmware		= config['firmware'] if( 'firmware' in config) else ''
		self.floorPlanId	= config['floorPlanId'] if( 'floorPlanId' in config) else ''
		
		self.hasValidIP		= False

		self.validateIpAddress()

	def validateIpAddress(self):
		try:
			ip_addr = ipaddress.ip_address(self.lanIp)
			self.hasValidIP = True
		except Exception:
			self.hasValidIP = False
		

	
	def hasValidIpAddress(self):
		return(self.hasValidIP)

	# To String	
	def __str__(self, showMatch=False):
		output = ''
		
		for key in self.__dict__:
			output += "[%s] -> [%s], " % (key, self.__dict__[key])

		return(output)

	# to XML
	def __toXml__(self):
		pass
	
	# To JSON
	def __toJson__(self):
		return(json.dump(self))

