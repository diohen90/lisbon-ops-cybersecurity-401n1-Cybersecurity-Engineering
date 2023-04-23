# Script : Challenge02.py
# Purpose: Python script that sends ICMP requests to a host to evaluate if they are up or down.
#!/usr/bin/python3

import time
import pythonping

while True:
    current_time = time.ctime()
    print("Current time is: %s" % current_time)