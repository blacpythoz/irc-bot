from xml.etree import cElementTree as ET
from urllib.request import urlopen 

## I need to learn more about xml.etree
## Only then It will be done

def get_rashi():
    res = urlopen("http://www.astrology.com/us/offsite/rss/daily-extended.aspx")
    raw=res.read()

#get_rashi()
