#!/usr/bin/python3

# 	Author: Buford Peek (<bupeek@cisco.com>)
#	Title:	Technical Solutions Architect
#

# General imports
import os
import sys
import traceback
import getopt


# updating my imports path
sys.path.append('./lib')

# importing Cisco Objects
from DeviceList import DeviceList


def Main(args):
	try:
		JSONFileName 	= 'default.json'
		ObjConfig		= {}

		# Parsing command line Arguments
		opts, args = getopt.getopt(args, "hf:")		

		# parsing the getopt option for configuration file only
		for option,value in opts:
			if ( option == '-f' ):
				JSONFileName = value
			elif ( option == '-h'):
				usage()
				return(0)
			else:
				usage()
				return(1)

		# Verifying that the file exists
		if not( os.path.exists(JSONFileName)):
			print("File [%s]: does NOT exists" % (JSONFileName) )
			return(1)
		
		ObjConfig['filename'] = JSONFileName
		
		devices = DeviceList(ObjConfig)
		devices.printIpValidity()
		
		return(0)
	
	except getopt.GetoptError as X:
		print(X)
		usage()
		return(1)

	except Exception as X:
		print(X)
		raise(traceback.format_exc())

	finally:
		print("Cisco Systems, Inc (c) (2020)")

# Usage
def usage():
	print ("\n - %s ------------------------------------" % (sys.argv[0]))
	print (" -f       JSON File")
	print (" -h       Help ")
	print ("\n")

if ( __name__ == '__main__' ):
	sys.exit(Main(sys.argv[1:]))
