import smtplib 
  
def trigger_mail(analysis):
    subject = 'Nifty 50 Analysis by Best Script tracker Tool'
    message = 'Subject: {}\n\n{}'.format(subject, analysis)
    toMailingList = ['131nimish@gmail.com"','nandu.chill06@gmail.com']

    print(analysis)

    s = smtplib.SMTP('smtp.gmail.com', 587) 
    s.ehlo()
    s.starttls() 
    s.login("bestscripttracker@gmail.com", "007nimish")
    s.sendmail("bestscripttracker@gmail.com", toMailingList, message)
    # print('message is ' + message)
    s.quit()
    print('Email sent successfully')