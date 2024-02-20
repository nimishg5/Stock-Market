import smtplib 
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