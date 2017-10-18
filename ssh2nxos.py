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
dev.close()



