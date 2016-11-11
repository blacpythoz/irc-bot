#! /usr/bin/env python3
# -*- coding: utf8 -*-
# To do
# Factorize code with classes and threds
from connector import Connection
import locale
import weather
import nepali_date
import os

# Get system default encodings
encoding = locale.getpreferredencoding()

bot = Connection()
bot.main()

def bot_reply(message,user):
    msg = message.split(' ')
    print(message)
    if msg[0] == "!fuck":
        bot.irc_send_priv("You ass hole, Mother fucker")

    if msg[0] == "!date":
        date = nepali_date.get_nepali_date()
        bot.irc_send_priv(date)

    if msg[0] == "!weather":
        if msg[-1] != msg[0]:
            condition = weather.get_weather(msg[1])
            bot.irc_send_priv("{} {}".format(user,condition))
        else:
            bot.irc_send_priv("{} Enter the city as :weather Kathmandu".format(user))

    # Change bot name through admin
    if user == bot.getadmin() and msg[0] == "!botnick":
        if msg[-1] != msg[0]:
            bot.irc_send("NICK {}".format(msg[1]))
        else:
            bot.irc_send_priv("Enter name of bot properly")

    # Exit the bots
    if user == bot.getadmin() and message == "kill bot":
        bot.irc_send("QUIT")


while True:
    buffer_msg= bot.irc_buffer_msg()

    # Respond ping message
    if buffer_msg.find("PING :") != -1:
        ping_value = buffer_msg.split(":")[1]
        bot.irc_send("PONG :{}".format(ping_value))

    if buffer_msg.find("PRIVMSG {} :{}:".format(bot.getchannel(), bot.getnick())) != -1:
        other_user = buffer_msg.split('!')[0]
        print("!!! PRIV msg found !!!")
        bot.irc_send("PRIVMSG {} :HELLO {}".format(bot.getchannel(), other_user))

    if buffer_msg.find("PRIVMSG {}".format(bot.getchannel())) != -1:
        other_user = buffer_msg.split('!')[0][1:]
        message = buffer_msg.split('PRIVMSG',1)[1].split(':',1)[1]
        bot_reply(message,other_user)

    print(buffer_msg)
