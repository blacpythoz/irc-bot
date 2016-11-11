#! /usr/bin/env python3
# -*- coding: utf8 -*-
# To do
# Factorize code with classes and threds

import weather
import nepali_date
from connector import Connection


class Bot():
    
    #connection object
    bot = ""

    def bot_reply(self,message,user):
        msg = message.split(' ')
        print(message)
        if msg[0] == "!fuck":
            self.bot.irc_send_priv("You ass hole, Mother fucker")

        if msg[0] == "!date":
            date = nepali_date.get_nepali_date()
            self.bot.irc_send_priv(date)

        if msg[0] == "!weather":
            if msg[-1] != msg[0]:
                condition = weather.get_weather(msg[1])
                self.bot.irc_send_priv("{} {}".format(user,condition))
            else:
                self.bot.irc_send_priv("{} Enter the city as :weather Kathmandu".format(user))

        # Change bot name through admin
        if user == self.bot.getadmin() and msg[0] == "!botnick":
            if msg[-1] != msg[0]:
                self.bot.irc_send("NICK {}".format(msg[1]))
            else:
                bot.irc_send_priv("Enter name of bot properly")

        # Exit the bots
        if user == self.bot.getadmin() and message == "kill bot":
            self.bot.irc_send("QUIT")

    def analyzeText(self,buffer_msg):
        # Respond ping message
        if buffer_msg.find("PING :") != -1:
            ping_value = buffer_msg.split(":")[1]
            self.bot.irc_send("PONG :{}".format(ping_value))

        if buffer_msg.find("PRIVMSG {} :{}:".format(self.bot.getchannel(), self.bot.getnick())) != -1:
            other_user = buffer_msg.split('!')[0]
            print("!!! PRIV msg found !!!")
            self.bot.irc_send("PRIVMSG {} :HELLO {}".format(self.bot.getchannel(), other_user))

        if buffer_msg.find("PRIVMSG {}".format(self.bot.getchannel())) != -1:
            other_user = buffer_msg.split('!')[0][1:]
            message = buffer_msg.split('PRIVMSG',1)[1].split(':',1)[1]
            self.bot_reply(message,other_user)

    def run(self):
        self.bot = Connection()
        self.bot.main()
        while True:
            buffer_msg = self.bot.irc_buffer_msg()
            self.analyzeText(buffer_msg)
            print(buffer_msg)

 
if __name__ == "__main__":
    bot = Bot()
    bot.run()

