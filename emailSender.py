import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
import appConstants

def trigger_mail(analysis):
    message = 'Subject: {}\n\n{}'.format(appConstants.MAIL_SUBJECT, analysis)

    s = smtplib.SMTP(appConstants.GMAIL_SPTP_URL, appConstants.GMAIL_SMTP_PORT)
    s.ehlo()
    s.starttls()
    s.login(appConstants.GMAIL_SMTP_LOGIN_ID, appConstants.GMAIL_SMTP_APP_PASSWORD)
    s.sendmail(appConstants.GMAIL_SMTP_LOGIN_ID, appConstants.TO_MAILING_LIST, message)
    # print('message is ' + message)
    s.quit()
    print(appConstants.MAIL_SEDNING_SUCCESS_MESSAGE)

def trigger_mail_2(analysis, file):
    fromaddr = appConstants.GMAIL_SMTP_LOGIN_ID
    toaddr = appConstants.TO_MAILING_LIST

    # instance of MIMEMultipart
    msg = MIMEMultipart()

    # storing the senders email address
    msg['From'] = fromaddr

    # storing the receivers email address
    msg['To'] = ", ".join(toaddr)

    # storing the subject
    msg['Subject'] = appConstants.MAIL_SUBJECT

    # string to store the body of the mail
    body = analysis

    # attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))

    # open the file to be sent
    filename = file
    attachment = open(file, "rb")

    # instance of MIMEBase and named as p
    p = MIMEBase('application', 'octet-stream')

    # To change the payload into encoded form
    p.set_payload((attachment).read())

    # encode into base64
    encoders.encode_base64(p)

    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    # attach the instance 'p' to instance 'msg'
    msg.attach(p)

    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    # Authentication
    s.login(fromaddr, appConstants.GMAIL_SMTP_APP_PASSWORD)

    # Converts the Multipart msg into a string
    text = msg.as_string()

    # sending the mail \
    s.sendmail(fromaddr, toaddr, text)

    # terminating the session
    s.quit()
    print(appConstants.MAIL_SEDNING_SUCCESS_MESSAGE)