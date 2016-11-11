#! /usr/bin/env python3
# -*- coding: utf8 -*-
# To do
# Factorize code with classes and threds
import socket
import ssl
import nepali_date
import weather
import nepali_date


# Values
host = 'irc.freenode.net'
port = 6697
nick = "Nepali_Babu"
username = "xxxxx123"
realname = "bot_d_panday"
modes = "2 3"
channelname = "##linuxnepal"
encoding = "UTF-8"
admin = "blacpythoz"

# Sockets  connection
irc_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
irc_sock.connect((host, port))

# Implement ssl connections
irc_sock = ssl.wrap_socket(irc_sock,ciphers=None)

def irc_send(msg):
    msg=msg+"\r\n"
    irc_sock.send(bytes(msg,encoding))

def irc_send_priv(msg):
    msg = msg+"\r\n"
    irc_sock.send(bytes("PRIVMSG {} :{}".format(channelname,msg), encoding))

irc_send("NICK {}".format(nick))
irc_send("USER {} {} {} :{}".format(username, modes, host, realname))
irc_send("JOIN {}".format(channelname))
irc_send_priv("blacpythoz HELLO!!".format(channelname))

def bot_reply(message,user):
    msg = message.split(' ')
    print(message)
    if msg[0] == "!fuck":
        irc_send_priv("You ass hole, Mother fucker")

    if msg[0] == "!date":
        date = nepali_date.get_nepali_date()
        irc_send_priv(date)

    if msg[0] == "!weather":
        if msg[-1] != msg[0]:
            condition = weather.get_weather(msg[1])
            irc_send_priv("{} {}".format(user,condition))
        else:
            irc_send_priv("{} Enter the city as :weather Kathmandu".format(user))

    # Change bot name through admin
    if user == admin and msg[0] == "!botnick":
        if msg[-1] != msg[0]:
            irc_send("NICK {}".format(msg[1]))
        else:
            irc_send_priv("Enter name of bot properly")

    # Exit the bots
    if user == admin and message == "kill bot":
        irc_send("QUIT")


while True:
    ## Receive the server output decode it and strip out the carriage return and newline
    buffer_msg = irc_sock.recv (1024).decode(encoding).strip('\n\r')

    # Respond ping message
    if buffer_msg.find("PING :") != -1:
        ping_value = buffer_msg.split(":")[1]
        irc_send("PONG :{}".format(ping_value))

    if buffer_msg.find("PRIVMSG {} :{}:".format(channelname, nick)) != -1:
        other_user = buffer_msg.split('!')[0]
        print("!!! PRIV msg found !!!")
        irc_send("PRIVMSG {} :HELLO {}".format(channelname, other_user))

    if buffer_msg.find("PRIVMSG {}".format(channelname)) != -1:
        other_user = buffer_msg.split('!')[0][1:]
        message = buffer_msg.split('PRIVMSG',1)[1].split(':',1)[1]
        bot_reply(message,other_user)

    print(buffer_msg)
