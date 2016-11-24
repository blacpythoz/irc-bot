#! /usr/bin/env python3
# To do # Implement Multi-Threading and caches

import threading
import weather
import nepali_date
from connector import Connection
from random import randint
import time
import jokes
import emailsender

# This is class bot it can to anythings
class Bot():
    
    #connection object
    bot = ""

    #User info
    users={}

    #local user to whom bot sents the message
    luser=""

    #xada work kolist
    words = ["mugi","mug","muji","randy","randi","radi","fuck","chikney","rando","kera","machis","lado","puti","muj",'chik',"machi","lundo","asshole","bitch","bhalu","myachis","myach"]

    # No of chance to give if words is spoken
    chance = 4

    # Message when user type !fuck
    fuckMessage = "You ass hole, Mother Fucker"

    # Just a function, it will be implemented as plugins later on
    def send_date(self,msg):
        date = nepali_date.get_nepali_date()
        self.sendMsg(date)

    def send_weather(self,msg):
        if len(msg) == 2:
            condition = weather.get_weather(msg[1])
            self.sendMsg(condition)
        else:
            self.sendMsg("Enter the city as  !weather Kathmandu")
    
    def send_email(self,msg,message):
        if len(msg) >= 3:
            message = ' '.join(msg[2:])
            data = emailsender.sentEmail(msg[1],message)
            if data == 1:
                self.sendMsg("Sent Successfully")
            else:
                self.sendMsg("Error in sending")
        else:
            self.sendMsg("Enter message as !email [emai-address] [message]")

    def send_jokes(self,msg):
        random = randint(0,8)
        print(random)
        if len(msg) == 2:
            joke = jokes.get_jokes(msg[1],random+1)
        else:
            joke = jokes.get_jokes(rand=random+1)
            print(joke[random])
            self.sendMsg(joke[random])

    def change_bot_name(self,msg):
        if len(msg) == 2:
            self.bot.irc_send("NICK {}".format(msg[1]))
        else:
            self.sendMsg("Enter name of bot properly")

    def change_fuck_message(self,msg):
        if len(msg) >= 2:
            message = ' '.join(msg[1:])
            self.fuckMessage = message 
        else:
            self.sendMsg("Enter the message as !fuckmsg [MESSAGE]")

    def bot_reply(self,message):
        print(self.luser)
        msg = message.split(' ')
        print(message)
        # the message starts with ! marks then it is command
        if message[0] == "!":
            # Just for fun [will be removed]
            if msg[0] == "!fuck":
                self.sendMsg(self.fuckMessage)

            # Provides the date 
            elif msg[0] == "!date":
                date=threading.Thread(target=self.send_date, args=(msg,))
                date.start()

            # Sends the weather info to user
            elif msg[0] == "!weather":
                weather=threading.Thread(target=self.send_weather, args=(msg,))
                weather.start()

            elif msg[0] == "!email":
                email = threading.Thread(target=self.send_email, args=(msg,message))
                email.start()

            elif msg[0] == "!jokes":
                jokes = threading.Thread(target=self.send_jokes, args=(msg,))
                jokes.start()

            # Change bot name through admin
            elif self.luser == self.bot.getadmin() and msg[0] == "!botnick":
                change_name = threading.Thread(target=self.change_bot_name, args=(msg,))
                change_name.start()

            # Change fuck message
            elif self.luser == self.bot.getadmin() and msg[0] == "!fuckmsg":
                fuck_msg = threading.Thread(target=self.change_fuck_message, args=(msg,))
                fuck_msg.start()

             # Provides help to the user
            elif msg[0] == "!help":
                self.sendMsg(" Currently available commads are !date, !weather location, !fuck, !jokes /tag/, !email [address] [message]  -[Admin Only]- : !fuckmsg [MSG] !botnick [NAME]  kill bot")
                self.bot.irc_send("NAMES {}".format(self.bot.getchannel()))
            # Exit the bots

            elif self.luser == self.bot.getadmin() and message == "kill bot":
                print(self.luser)
                self.bot.irc_send("QUIT")
            else:
                self.sendMsg("Unknown command: Type !help for more info")
        else:
            check_kick=threading.Thread(target=self.testKick, args=(message,))
            check_kick.start()

    def analyzeText(self,msg):
        # Respond ping message
        if msg.find("PING :") != -1:
            ping_value = msg.split(":")[1]
            self.bot.irc_send("PONG :{}".format(ping_value))

        if msg.find("PRIVMSG {}".format(self.bot.getchannel())) != -1:
            self.luser = msg.split('!')[0][1:]
            message = msg.split('PRIVMSG',1)[1].split(':',1)[1]
            self.bot_reply(message)

    # Kick user if the speak rude words
    # Function determines whether to kick the guy or not
    def testKick(self,msg):
        if any(word in msg.lower() for word in self.words):
            if self.luser in self.users:
                self.users[self.luser] += 1
                if self.users[self.luser] == self.chance:
                    self.bot.irc_send("PRIVMSG chanserv :op {}".format(self.bot.getchannel()))
                    time.sleep(2)
                    self.bot.irc_send("KICK {} {}".format(self.bot.getchannel(),self.luser))
                    time.sleep(1)
                    self.bot.irc_send("PRIVMSG chanserv :deop {}".format(self.bot.getchannel()))
                    self.users.pop(self.luser)
                    return
                self.sendMsg("You have {} chances".format(self.chance - self.users[self.luser])) 
            else:
                self.users[self.luser] = 0

    # This functions sent the message to user directly
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
