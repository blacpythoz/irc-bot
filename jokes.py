#! /usr/bin/env python3
import bs4
import json
import requests

#
#All the information are taken from onlinefun.com
#

tag = ['age','attitude','communication','fat','food','god','health','drug','health','flirty','sex','stupid','dirty']

def get_jokes(title="dirty",rand=2):
    # Check if unknow value is entered
    if title not in tag:
        title = "dirty"
    res = requests.get("http://onelinefun.com/{}/{}/".format(title,rand))
    soup = bs4.BeautifulSoup(res.text,"html.parser")
    data = soup.findAll("p")

    datas = []

    for dat in data[1:10]:
        datas.append(dat.text)
        print(dat.text)

    return datas

#get_jokes()
