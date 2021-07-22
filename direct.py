
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(
    from_email=('FROM-EMAIL','NAME'),
    to_emails='TP-EMAIL',
    subject="SUBJECT",
    html_content='EMAIL-CONTENT')
sg = SendGridAPIClient('SEND-GRID-API')
response = sg.send(message)
print(response.status_code)
print(response.body)
print(response.headers)
