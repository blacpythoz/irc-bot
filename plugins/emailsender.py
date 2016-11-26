import smtplib

def sentEmail(address,message):
    sender = 'ircemailclient@gmail.com'
    sender_pass='subasharyal'
    receivers = address

    try:
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(sender,sender_pass)
        server.sendmail(sender,receivers,message)
        print("Send")
        return 1
    except :
        print("not send")
        return 0

#sentEmail('blacpythoz@gmail.com','Hello Mother Fucker')
