#! /usr/bin/env python3
import json
from urllib.request import urlopen
import xml.etree.ElementTree as et

def get_data():
    #web_data = urlopen("http://english.onlinekhabar.com/feed/")
    web_data = urlopen("http://www.astrology.com/us/offsite/rss/daily-extended.aspx")
    #web_data = urlopen("http://www.w3schools.com/xml/cd_catalog.xml")
    str_data = web_data.read()

    xml_data = et.fromstring(str_data)
    cd_list = xml_data.findall("item")
    for k in cd_list:
        print(k.find("title").text)
    print(list(cd_list))


#get_data()
