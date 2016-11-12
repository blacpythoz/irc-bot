#! /usr/bin/env python3
import bs4
import requests

#
#All the information are taken from onlinefun.com
#

def get_jokes():
    res = requests.get("http://onelinefun.com/")
    soup = bs4.BeautifulSoup(res.text,"html.parser")
    data = soup.findAll("p")

    datas = []
    for dat in data[1:10]:
        datas.append(dat.text)

    return datas

#get_jokes()
