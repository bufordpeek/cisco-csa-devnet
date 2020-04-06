#!/usr/bin/python3

# General imports
import os
import sys
import traceback
import getopt

def Main(args):
	try:
				
		return(0)	

	except Exception as X:
		print(X)
		raise(traceback.format_exc())
		

	finally:
		print("Cisco Systems, Inc (c) (2020)")

# Usage
def usage():
	print (sys.argv[0])

if ( __name__ == '__main__' ):
	sys.exit(Main(sys.argv[1:]))
