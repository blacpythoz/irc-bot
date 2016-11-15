import weechat
import subprocess

# How to install
# Copy this file in .weechat/python by:
# cp weechat_plugin .weechat/python/
# if there is no .weechat/python create one:
# mkdir -p .weechat/python/autoload
# Then go to .weechat/python/autoload/
# cd .weechat/python/autoload/
# Then symbolic to weechat_plugin.py by executing following code:
# ln -s ../weechat_plugin.py

## Testing the functions
weechat.prnt("",",  from python script!")

SCRIPT_NAME = "Testing"
SCRIPT_AUTHOR = "Subash"
SCRIPT_VERSION = "0.1"
SCRIPT_LICENSE = "Free"
SCRIPT_DESC = "Execute any commands"

# Your nick in irc
nick = "blacpythoz"

# Var
weechat.register(
        SCRIPT_NAME,
        SCRIPT_AUTHOR,
        SCRIPT_VERSION,
        SCRIPT_LICENSE,
        SCRIPT_DESC,
        "",""
)

def playFile(data,signal,signal_data):
    message=signal_data.split("PRIVMSG")[1].split(":",1)[1]
    msg = message.split(" ")
    if msg[0][0]== '>' and len(msg) == 3:
        if msg[0] == '>play' and msg[2] ==nick: 
            ##Debugging
            weechat.prnt("",message)
            weechat.prnt("",msg[0])
            weechat.prnt("",msg[1])
            weechat.prnt("",msg[2])
            try:
                weechat.prnt("","Playing with vlc")
                subprocess.Popen(["vlc",msg[1]],stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
            except:
                weechat.prnt("","Error: Occurred")
        if msg[0] == '>url' and msg[2] ==nick: 
            try:
                weechat.prnt("","Playing with web-browser")
                subprocess.Popen(["xdg-open",msg[1]],stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
            except:
                weechat.prnt("","Error: Occurred")
        else:
            server = signal.split(",")[0]
            channel = signal_data.split(":")[-1]
            buffer = weechat.info_get("irc_buffer", "%s,%s" % (server,channel))
            weechat.prnt(buffer,"Enter in form >play [url] [nickName]")
    return weechat.WEECHAT_RC_OK

weechat.hook_signal("*,irc_in_privmsg","playFile","")
