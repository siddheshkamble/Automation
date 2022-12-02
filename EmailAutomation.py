import os
from email.message import EmailMessage
import ssl
import smtplib
import schedule
from sys import *
import time

def Task_Minute():
    print("Email send")

    email_sender = 'Sender@gmail.com'
    email_password = 'XXXXpasswordXXXXX'
    email_receiver = 'reciver@gmail.com '

    subject = 'This is Email Automation'
    body = """
    Email message
    """
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())

def main():
    print("Email Automation")

    schedule.every(1).minutes.do(Task_Minute)

    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()

