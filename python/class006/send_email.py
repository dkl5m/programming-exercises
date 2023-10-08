#!/usr/bin/env python
# coding:utf-8
# ln[]:

"""
To tell Google to create a password for sending emails:

. click on your profile > Manage your google account
. go to Security.
. scroll down until you find the banner with "How to sign in to Google"
. first do the two-step verification and go to the next step.
. when enabling two-step verification, click on app passwords.
. login google login.
. select the Email app and the name of the device that will send email.
    I suggest putting it in Other and putting a specific name
    and click generate. When you click on generate, a password will appear,
    copy it and paste it into the Password field of the code you send below.
"""

import smtplib
import ssl
import email.message


def send_email():
    body = """
    <p>---- Email body ----</p>
    """

    # Message
    msg = email.message.Message()
    msg['Subject'] = "Subject"
    msg['From'] = 'Sender_email'
    msg['To'] = 'Recipient_email'
    password = 'Your_password'  # The way explained above
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(body)

    context = ssl.create_default_context()
    connections = smtplib.SMTP('smtp.gmail.com:587')
    connections.ehlo()
    connections.starttls(context=context)

    # Login credentials for sending the mail
    connections.login(msg['From'], password)
    connections.sendmail(msg['From'], msg['To'],
                         msg.as_string().encode('utf-8'))
    print('Email sent!')

# ln[]:


send_email()
