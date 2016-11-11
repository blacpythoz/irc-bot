import bs4
import requests

def get_nepali_date():
    res = requests.get("http://nepalipatro.com.np/language/switch/to/1?redirect=/")
    soup = bs4.BeautifulSoup(res.text,"html.parser")
    data = soup.find("div", {"class":"today"})
    data_list = data.text.split('\n')[1:8]
    text = "["+data_list[6]+"]  "+data_list[2]+"/"+data_list[0]+"/"+data_list[1]+"  "+data_list[3]+"  -"+data_list[4]

    return text

    #for data in data_list:
        #print(data)
