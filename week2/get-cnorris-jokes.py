#!/usr/bin/python3

# 	Author: Buford Peek (<bupeek@cisco.com>)
#	Title:	Technical Solutions Architect
#

# General imports
import os
import sys
import traceback
import getopt

# Imports
import requests
import json

def Main(args):
	try:
		# Chuck Norris API http
		cnorrisAPI 		= 'https://api.chucknorris.io/jokes/random'
		cnorrisJson 	= ''	
		cnorrisJoke		= ''

		# Chuck Norris Requests
		cnorrisRequest = requests.get(cnorrisAPI)

		if ( cnorrisRequest.status_code == 200 ):
			cnorrisJson	   	= json.loads(cnorrisRequest.text)
			cnorrisJoke 	= cnorrisJson['value']; 
		

		print("\n--------\n %s \n--------\n" % (cnorrisJoke))
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
