from getpass import getpass
import smtplib
from email.message import EmailMessage

# Create an email
emailObject = EmailMessage()
emailObject['Subject'] = input("Subject: ")
emailObject['From'] = input("Your Email: ")
emailObject['To'] = input("To: ")
emailObject.set_content(input("Message: "))

# Send the message
smtp = smtplib.SMTP('smtp.gmail.com', 587)
smtp.starttls()
app_password = getpass("Your Google App Password: ")
smtp.login(emailObject['From'], app_password)
smtp.send_message(emailObject)
smtp.quit()