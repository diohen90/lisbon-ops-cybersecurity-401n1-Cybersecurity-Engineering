# Script : Challenge03.py
# Purpose: Python script that sends emails to an email address.
# Why: Automate emails.
#!/usr/bin/python3

import smtplib

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)

email_sender = input ("Insert your email: ")
email_password = input ("Insert your password: ")
email_receiver = "jegvpczrvskybgb@bugfoo.com"

server.login(email_sender, email_password)
