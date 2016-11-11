#! /usr/bin/env python3
# -*- coding: utf8 -*-
# To do
# Factorize code with classes and threds
import locale
import weather
import nepali_date
import os
import irc

# Get system default encodings
encoding = locale.getpreferredencoding()

botObj = irc.Irc()
botObj.main()

def bot_reply(message,user):
    msg = message.split(' ')
    print(message)
    if msg[0] == "!fuck":
        botObj.irc_send_priv("You ass hole, Mother fucker")

    if msg[0] == "!date":
        date = nepali_date.get_nepali_date()
        botObj.irc_send_priv(date)

    if msg[0] == "!weather":
        if msg[-1] != msg[0]:
            condition = weather.get_weather(msg[1])
            botObj.irc_send_priv("{} {}".format(user,condition))
        else:
            botObj.irc_send_priv("{} Enter the city as :weather Kathmandu".format(user))

    # Change bot name through admin
    if user == botObj.getadmin() and msg[0] == "!botnick":
        if msg[-1] != msg[0]:
            botObj.irc_send("NICK {}".format(msg[1]))
        else:
            botObj.irc_send_priv("Enter name of bot properly")

    # Exit the bots
    if user == botObj.getadmin() and message == "kill bot":
        botObj.irc_send("QUIT")


while True:
    ## Receive the server output decode it and strip out the carriage return and newline
    buffer_msg= botObj.irc_buffer_msg()

    # Respond ping message
    if buffer_msg.find("PING :") != -1:
        ping_value = buffer_msg.split(":")[1]
        botObj.irc_send("PONG :{}".format(ping_value))

    if buffer_msg.find("PRIVMSG {} :{}:".format(botObj.getchannel(), botObj.getnick())) != -1:
        other_user = buffer_msg.split('!')[0]
        print("!!! PRIV msg found !!!")
        botObj.irc_send("PRIVMSG {} :HELLO {}".format(botObj.getchannel(), other_user))

    if buffer_msg.find("PRIVMSG {}".format(botObj.getchannel())) != -1:
        other_user = buffer_msg.split('!')[0][1:]
        message = buffer_msg.split('PRIVMSG',1)[1].split(':',1)[1]
        bot_reply(message,other_user)

    print(buffer_msg)
