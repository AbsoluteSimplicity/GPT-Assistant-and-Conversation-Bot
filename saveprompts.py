import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE
from email import encoders

# Email login credentials
USERNAME = 'leonardo.kulon@gmail.com'
PASSWORD = 'LeoIsABear1!1!'
def save_history():
    # Email content
    msg = MIMEMultipart()
    msg['From'] = USERNAME
    msg['To'] = COMMASPACE.join(['leonardo.kulon@gmail.com'])
    msg['Subject'] = 'Prompt'

    # Attach a file
    filename = 'history.txt'
    attachment = open(filename, 'rb')
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(part)

    # Send the email
    smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
    smtp_server.ehlo()
    smtp_server.starttls()
    smtp_server.login(USERNAME, PASSWORD)
    smtp_server.sendmail(USERNAME, 'recipient_email_address', msg.as_string())
    smtp_server.close()
