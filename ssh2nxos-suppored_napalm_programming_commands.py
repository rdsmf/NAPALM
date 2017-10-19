#!/usr/local/bin/python

# Sample NAPALM SCRIPT TO TEST SSH CONNECTIVITY TO NXOS
#NAPALM Network Drivers (https://napalm.readthedocs.io/en/latest/base.html?highlight=https%20request)
import napalm
import sys
import json
import os
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
from napalm import get_network_driver
driver = get_network_driver('nxos') #Supported devices (https://napalm.readthedocs.io/en/latest/support/index.html)

#DEVICE DEFINITIONS
dev = driver(hostname='<ip address>', username='<user>', password='<password>')
dev.open()

#Define variable to print in JSON notation
<variable name> = dev.<variable name>() #List of supported variables (https://napalm.readthedocs.io/en/latest/base.html)
print(json.dumps(<variable nam>, sort_keys=True, indent=4))

#Close SSH connection to device
dev.close()


#Example NAPALM programming command to get BGP neighbors

#Define variable to print in JSON notation
#bgp_neighbors = dev.get_bgp_neighbors()
#print(json.dumps(bgp_neighbors, sort_keys=True, indent=4))
#dev.close()
