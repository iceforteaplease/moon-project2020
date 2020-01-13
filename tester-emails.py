# this code works!!!
# import smtplib, ssl
#
# port = 465  # For SSL
# smtp_server = "smtp.gmail.com"
# sender_email = "pythontesting2020learning@gmail.com"  # Enter your address
# receiver_email = "pythontesting2020learning@gmail.com"  # Enter receiver address
# password = input("Type your password and press enter: ")
# message = """\
# Subject: Hi there
#
# This message is sent from Python."""
#
# context = ssl.create_default_context()
# with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
#     server.login(sender_email, password)
#     server.sendmail(sender_email, receiver_email, message)

# this code works too!!! sends multiple attachmeents
import email, smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

subject = "An email with attachment from Python"
body = "This is an email with attachment sent from Python"
sender_email = "pythontesting2020learning@gmail.com"
receiver_email = "pythontesting2020learning@gmail.com"
password = input("Type your password and press enter:")
if password == '' :
    password = '123$test'

# Create a multipart message and set headers
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message["Bcc"] = receiver_email  # Recommended for mass emails

# Add body to email
message.attach(MIMEText(body, "plain"))

# filename = "raw-data.txt"  # In same directory as script
filenames = ['raw-data.txt', 'test-calcs.txt']
# Open PDF file in binary mode
for each in filenames :
    with open(each, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {each}",
    )

    # Add attachment to message and convert message to string
    message.attach(part)
text = message.as_string()

# Log in to server using secure context and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, text)

print('email sent') #sent only one and flipped the info in txt file, figure that out
