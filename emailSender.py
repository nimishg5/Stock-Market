import smtplib 
  
def trigger_mail(message):
    s = smtplib.SMTP('smtp.gmail.com', 587) 
    s.ehlo()
    s.starttls() 
    s.login("bestscripttracker@gmail.com", "007nimish") 
    s.sendmail("bestscripttracker@gmail.com", "131nimish@gmail.com", message)
    print('message is ' + message)
    s.quit()
    print('Email sent successfully')