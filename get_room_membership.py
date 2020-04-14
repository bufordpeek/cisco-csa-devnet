#!/usr/bin/python3

#
#	Author: Buford Peek <bupeek@cisco.com> - Technical Solutions Architect
#
#

# Pyhton imports
import os
import sys

# HTTP imports
import requests

#JSON import
import json

# Global Parameters
roomID			= 'Y2lzY29zcGFyazovL3VzL1JPT00vNWJiMmRiZjAtNmFkOC0xMWVhLWEzNmEtMDc0ZjMxN2Y0Njli'
bearer 			= ''
membership_url 	= 'https://api.ciscospark.com/v1/memberships/'

#Authorization Header
authHeader		= { 'Accept' 		: 'application/json',
					'Content-Type'	: 'application/json',
					'Authorization' : 'Bearer ' + bearer
				}

# Setting my CGI Parameters
m = { 'roomId' : roomID,
	  'max'		: 500 } 

# Pulling user data from
r = requests.get( membership_url, params=m, headers=authHeader )


# Getting the data
people_req_json = json.loads(r.text)

# pulling people json out of requests json
people_json = people_req_json['items']

# Iterating through the people jason and printing in csv format
for people in people_json:
    print people['personDisplayName'] + ",<" + people['personEmail'] + ">"
