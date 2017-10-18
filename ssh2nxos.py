# Sample NAPALM SCRIPT TO TEST SSH CONNECTIVITY TO NXOS
import napalm
import sys
import json
import os
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
from napalm import get_network_driver
driver = get_network_driver('nxos')

#DEVICE DEFINITIONS
dev = driver(hostname='<ip address>', username='<username>', password='<password>')
dev.open()
dev.close()



