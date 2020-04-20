#!/usr/bin/python3


#
# Author: Buford Peek (bupeek@cisco.com)
#         Technical Solutions Architect


# python imports
import os
import sys

# updating the path
sys.path.append('/lancope/das/lib')


# Class Definition
class ApplianceInfo(): 
	
	# default construstor
	def __init__(self, config=dict()):
		pass		
		
	# To String	
	def __str__(self, showMatch=False):
		pass		

	# to XML
	def __toXml__(self):
		pass
	
	# To JSON
	def __toJson__(self):
		pass

