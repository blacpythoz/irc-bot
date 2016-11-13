import smtplib

def sentEmail(address,message):
    sender = '#####@gmail.com'
    sender_pass='#######'
    receivers = address

    try:
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(sender,sender_pass)
        server.sendmail(sender,receivers,message)
        return 1
    except :
        return 0

#sentEmail('blacpythoz@gmail.com','Hello Mother Fucker')
