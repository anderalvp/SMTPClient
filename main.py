import smtplib, ssl, email
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#Start a SMTP connection secured by SSL (Secure Sockets Layer)
context = ssl.create_default_context()
port = 465
password = input('Type your password and press enter\n')

#Fire up the server session and login
server = smtplib.SMTP_SSL("smtp.gmail.com", port, context = context)
server.ehlo()
server.login("s3nd3r.9009@gmail.com", password)

message = MIMEMultipart()
message['From'] = 'Aristotle'
message['To'] = 'Gilbert'
message['Subject'] = 'SMTP Client Test with Python'

#Plain text message
text = """\
Hi Gilbert!
How are you?
This is a SMTP Test"""

#Convert the text into MIMEText object
msg = MIMEText(text, "plain")

#Add plain text message to the MIMEMultipart
message.attach(msg)

#Attach a PDF file
filename = "2. SMTP Client/document.pdf"
attachment = open(filename, 'rb')
file = MIMEBase('application', 'octet-stream')
file.set_payload(attachment.read())

#Encode the file in ASCII characters
encoders.encode_base64(file)

#Add a header to the attachment file
file.add_header("Content-Disposition", f"attachment; filename= {filename}")

#Add filename.pdf to the MIMEMultipart
message.attach(file)

#Send email 
doc = message.as_string()
server.sendmail('s3nd3r.9009@gmail.com', 'r3c3iv3r.9009@gmail.com', doc)

