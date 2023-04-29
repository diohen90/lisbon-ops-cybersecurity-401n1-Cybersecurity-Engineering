#!/usr/bin/python3
# Script : Challenge02.py
# Purpose: Python script that sends ICMP requests to a host to evaluate if they are up or down.
# Why: Automate ICMP requests with date and time stamps.

import time
import os
from datetime import datetime

# IP address to ping
ip = '8.8.8.8'
# Time interval between pings
interval = 2

while True:
    # Current timestamp
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')

    # Send the ICMP packet and get the return status
    status = os.system(f'ping -c 1 {ip} > /dev/null 2>&1')

    # Evaluate the return status and assign a success or failure status
    if status == 0:
        status_text = 'Success'
    else:
        status_text = 'Failure'

    # Print the status and timestamp
    print(f'{now} - {ip}: {status_text}')
    # Wait for the specified interval before sending the next ICMP packet
    time.sleep(interval)
