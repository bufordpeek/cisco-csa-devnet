#!/usr/bin/python3


#
# Author: Buford Peek (bupeek@cisco.com)
#         Technical Solutions Architect


# python imports
import os
import sys

# extended imports
import json

# updating the path
sys.path.append('.')
sys.path.append('lib/')

from TestDevice import TestDevice

# Class Definition
class DeviceList(): 
	
	# default construstor
	def __init__(self, config=dict()):
		self.filename 		= config['filename']
		self.devices		= []
		self.deviceData		= ''

		# File Checking
		if not( os.path.exists(self.filename) ):
			raise('File: [%s] does NOT exists!' %  (self.filename) )

		# Opening File
		jsonFD = open(self.filename)
	
		# Loading Json Object
		self.deviceData =  json.load(jsonFD)

		for device in self.deviceData:
			self.devices.append(TestDevice( dict(device) ) )
	
	def printIpValidity(self):
		for device in self.devices:
			if( device.hasValidIpAddress() ):
				print( "[%s] is a valid IP for Device Serial [%s]" % (device.lanIp, device.serial) )
			else:
				print( "[%s] is NOT a valid IP for Device Serial [%s]" % (device.lanIp, device.serial) )


	# To String	
	def __str__(self, showMatch=False):
		pass

	# to XML
	def __toXml__(self):
		pass
	
	# To JSON
	def __toJson__(self):
		pass

