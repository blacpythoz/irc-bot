#! /usr/bin/env python3
#! -*- encoding: utf8  -*-

import socket
import ssl
import os
import json
import locale

# Get system default encodings
encoding = locale.getpreferredencoding()

myfile='bot.config'
#config_files =os.path.join(os.getcwd(),myfile) 
config_files ='/home/deadsec/code/irc/'+myfile
print(config_files)

# Values
default_value = {
        "host":"irc.freenode.net",
        "port": 6697,
        "nick":"mRobot123",
        "username":"xxxxx123",
        "realname":"bot_d_panday",
        "modes":"2 3",
        "channelname":"##linuxnepal",
        "encoding":"UTF-8",
        "admin":"blacpythoz",
}

def create_config_file():
    if os.path.isfile(config_files) == False:
        with open(config_files,'w') as f:
            json.dump(default_value,f,sort_keys=True,indent=4)
            print("Config files created")
    else:
        print("Files exists")

class Connection():

    setting = False
    sock = ""

    def load_prefers(self):
        if os.path.isfile(config_files):
            with open(config_files) as f:
                self.setting = json.load(f)
        else:
            self.setting = default_value

    def sock_connection(self):
        irc_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        irc_sock.connect((self.setting["host"], self.setting["port"]))
        print("Created sock")
        return irc_sock

    # Implement ssl connections
    def ssl_connection(self):
        connect = self.sock_connection()
        print("MAde ssl connection")
        return ssl.wrap_socket(connect,ciphers=None)

    def irc_send(self,msg):
        msg=msg+"\r\n"
        self.sock.send(bytes(msg,self.setting["encoding"]))

    def irc_send_priv(self,msg):
        msg = msg+"\r\n"
        self.sock.send(bytes("PRIVMSG {} :{}".format(self.setting["channelname"],msg), self.setting["encoding"]))

    # Receive the server output decode it and strip out the carriage return and newline
    def irc_buffer_msg(self):
        buffer_msg = self.sock.recv (1024).decode(self.setting["encoding"]).strip('\n\r')
        return buffer_msg

    def getchannel(self):
        return self.setting["channelname"]

    def getadmin(self):
        return self.setting["admin"]

    def getnick(self):
        return self.setting["nick"]

    def main(self):
        self.load_prefers()
        self.sock = self.ssl_connection()

        self.irc_send("NICK {}".format(self.setting["nick"]))
        self.irc_send("USER {} {} {} :{}".format(self.setting["username"], 
                                                     self.setting["modes"], 
                                                     self.setting["host"], 
                                                     self.setting["realname"]))
        self.irc_send("JOIN {}".format(self.setting["channelname"]))
        self.irc_send_priv("blacpythoz HELLO!!".format(self.setting["channelname"]))

# For testing connections
if __name__ == "__main__":
    k = Connection()
    k.main()
