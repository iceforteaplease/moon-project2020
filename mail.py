import gspread
from oauth2client.service_account import ServiceAccountCredentials


scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

name = 'testing'
sheet = client.open(name).sheet1
data = sheet.get_all_records(empty2zero=True, head=2)

print(data)

# change blanks to zeros, might not need this anymore
# for each in data :
#     # print(each)
#     for k,v in each.items() :
#         if v == '':
#             v = 0
        # print('key:', k, 'value:', v)

# calculate total
# total = 0
# for each in data:
#     for key,value in each.items():
#         try:
#             num = int(value)
#         except:
#             continue
#         total = total + num
#
# print(total)

# this gets the month number successfully and month/year for email
import datetime
from datetime import date

today = datetime.date.today()
str_today = str(today)

month_year_for_email = str_today[5:8] + str_today[:4]

month = str_today[5:7]

if month[0] == '0' : # makes one digit if first number is 0
    month = month[1:2]
int_month = int(month)
# print(int_month)

# making files see file-create.py
# f1 = open('raw-data.txt', 'w+')
# head = ['day | ', 'item1 | ', 'item2\n']
# f1.writelines(head)
# for each in data :
#     for k,v in each.items() :
#         lines = [str(v), ' |   ']
#         f1.writelines(lines)
#
#
# f2 = open('test-calcs.txt', 'w+')
# strlst2 = ['Total: ', str(total)]
# f2.writelines(strlst2)
# print('files created')
#
# f1.close()
# f2.close()

# email files
import email, smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

subject = "Waste Data South 1st " + month_year_for_email
body = "Automated email. Attached are the files containing the data from this months sheet, and the total number of wasted items"
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
# use try/exepct to prevent traceback
context = ssl.create_default_context()
try :
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)
except :
    print('Problem sending email')
    quit()
print('email sent')
