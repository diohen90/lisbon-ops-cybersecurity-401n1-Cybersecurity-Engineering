#!/usr/bin/python3
# Script : Challenge03.py
# Purpose: Python script that sends emails to an email address.
# Why: Automate emails.


import os
import smtplib
import time
from datetime import datetime
from email.mime.text import MIMEText

# Email server details
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)

# Host IP
ip = '8.8.8.8'

# Define the time interval for sending ICMP packets (in seconds)
interval = 2

# Enter user email, password and receiver of email
email_sender = input ("Insert your email: ")
email_password = input ("Insert your password: ")
email_receiver = "jegvpczrvskybgb@bugfoo.com"

server.login(email_sender, email_password)

# Define the email message
msg_template = 'Host {ip} changed status from {old_status} to {new_status} at {timestamp}'
msg = MIMEText('')
msg['Subject'] = 'Host Status Change Notification'
msg['From'] = email_sender
msg['To'] = email_receiver

# Initialize the host status to "down"
old_status = 'down'

while True:
    # Get the current timestamp
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')

    # Send the ICMP packet and get the return status
    status = os.system(f'ping -c 1 {ip} > /dev/null 2>&1')

    # Evaluate the return status and assign a success or failure status
    if status == 0:
        new_status = 'up'
    else:
        new_status = 'down'

    # Check if the status has changed
    if old_status != new_status:
        # Update the email message with the new status information
        msg.set_payload(msg_template.format(ip=ip, old_status=old_status, new_status=new_status, timestamp=now))

        # Send the email notification
        server.send_message(msg)

        # Print the status change and timestamp
        print(f'{now} - {ip} changed status from {old_status} to {new_status}')

        # Update the old status to the new status
        old_status = new_status

    # Wait for the specified interval before sending the next ICMP packet
    time.sleep(interval)
    server.quit()