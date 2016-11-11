#! /usr/bin/env python3
# -*- coding: utf8 -*-

import json
from urllib.request import urlopen

# Obtain the access tokens from the developer.facebook
# its a access token in the format    app_id|app_secret
with open("token") as f:
    # app_id | app_secret
    access=f.read()

#number of post
num = 5

f = urlopen("https://graph.facebook.com/v2.5/islingtoncollege/feed?access_token={}".format(access))

json_string = f.read().decode('utf8')
f.close()
parsed_json = json.loads(json_string)
for keys in parsed_json["data"][2:5]:
    print("-"*5,end=" ")
    print(keys["created_time"][:10],end=" ")
    print("-"*5)
    try:
        print(" ".join(keys["message"].split()),"\n")
    except:
        print(keys["story"].strip(),"\n")
