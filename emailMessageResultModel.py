
emailMessage = "Here is the full Analysis for the Nifty 50 stocks : "

def setEmailMessage(message):
    global emailMessage
    emailMessage += '\n' + message

def getEmailMessage():
    return emailMessage