#!/usr/bin/python3

#pip3 install sendgrid
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(
    from_email=('support@example.com','Support'),
    to_emails='victim@example.com',
    subject="PUT YOUR SUBJECT",
    html_content='PUT YOUR CONTENT HERE')
sg = SendGridAPIClient('PUT YOUR SENDGRID API HERE')
response = sg.send(message)
print(response.status_code)
print(response.body)
print(response.headers)
