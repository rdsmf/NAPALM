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
dev = driver(hostname='192.168.250.6', username='admin', password='Pl3xeCu73!')
dev.open()


