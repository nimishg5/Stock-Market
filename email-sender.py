import smtplib 
  
def trigger_mail(message):
    s = smtplib.SMTP('smtp.gmail.com', 587) 
    s.ehlo()
    s.starttls() 
    s.login("nimishfaadu@gmail.com", "idontbelieve") 
    s.sendmail("nimishfaadu@gmail.com", "131nimish@gmail.com", message) 
    s.quit()
    print('Email sent successfully')