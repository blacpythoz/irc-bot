import socket
import ssl

# Values
host = 'irc.freenode.net'
port = 6667
nick = "deadlyVirus"
username = "dengy23hell"
realname = "VioleDpanday"
modes = "2 3"
channelname = "##linuxnepal"
encoding = "UTF-8"

# Sockets  connection
irc_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
irc_sock.connect((host, port))

# Implement ssl connections
# irc_sock = ssl.wrap_socket(irc_sock,ciphers=None)

def irc_send(msg):
    msg=msg+"\r\n"
    irc_sock.send(bytes(msg,encoding))

irc_send("NICK %s" % nick)
irc_send("USER %s %s %s :%s" % (username, modes, host, realname))
irc_send("JOIN %s" % channelname);
irc_send("PRIVMSG ##linuxnepal blacpythoz HELLO!!")

while True:
    ## Receive the server output decode it and strip out the carriage return and newline
    buffer_msg = irc_sock.recv (1024).decode(encoding).strip('\n\r')

    # Respond ping message
    if buffer_msg.find("PING :") != -1:
        ping_value = buffer_msg.split(":")
        print("Pinging back",ping_value[1])
        irc_send("PONG :%s" % ping_value[1])

    if buffer_msg.find("PRIVMSG %s :%s:" %(channelname, nick)) != -1:
        other_user = buffer_msg.split('!')
        print("!!! PRIV msg found !!!")
        irc_send("PRIVMSG %s :HELLO %s" %(channelname, other_user[0]))

    print(buffer_msg)
