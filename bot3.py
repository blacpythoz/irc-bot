#! /usr/bin/env python3
# -*- coding: utf8 -*-
# To do
# Factorize code with classes and threds

import weather
import nepali_date
from connector import Connection


# This is class bot it can to anythings
class Bot():
    
    #connection object
    bot = ""

    #local user to whom bot sents the message
    luser=""

    def bot_reply(self,message,user):
        msg = message.split(' ')
        print(message)
        # the message starts with ! marks then it is command
        if msg[0][0] == "!":
            if msg[0] == "!fuck":
                self.sendMsg("You ass hole, Mother fucker")

            elif msg[0] == "!date":
                date = nepali_date.get_nepali_date()
                self.sendMsg(date)

            elif msg[0] == "!weather":
                if len(msg) == 2:
                    condition = weather.get_weather(msg[1])
                    self.sendMsg(condition)
                else:
                    self.sendMsg("Enter the city as  !weather Kathmandu")

            # Change bot name through admin
            elif user == self.bot.getadmin() and msg[0] == "!botnick":
                if msg[-1] != msg[0]:
                    self.bot.irc_send("NICK {}".format(msg[1]))
                else:
                    self.sendMsg("{}Enter name of bot properly")

            elif msg[0] == "!help":
                self.sendMsg(" Currently available commads are !date, !weather [location], !fuck")

            # Exit the bots
            elif user == self.bot.getadmin() and message == "kill bot":
                self.bot.irc_send("QUIT")

            else:
                self.sendMsg("Unknown command: Type !help for more info")

    def analyzeText(self,msg):
        # Respond ping message
        if msg.find("PING :") != -1:
            ping_value = msg.split(":")[1]
            self.bot.irc_send("PONG :{}".format(ping_value))

        if msg.find("PRIVMSG {}".format(self.bot.getchannel())) != -1:
            user = self.getusername(msg)
            message = msg.split('PRIVMSG',1)[1].split(':',1)[1]
            self.bot_reply(message,user)

    # This functions returns the username 
    def getusername(self,msg):
        self.luser = msg.split('!')[0][1:]

    # THis functions sent the message to user directly
    def sendMsg(self,msg):
        self.bot.irc_send_priv("{} {}".format(self.luser,msg))

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

