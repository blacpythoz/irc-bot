import bs4
import requests

res = requests.get("http://nepalipatro.com.np/language/switch/to/1?redirect=/")
soup = bs4.BeautifulSoup(res.text,"html.parser")
data = soup.find("div", {"class":"today"})
data_list = data.text.split('\n')[1:8]

for data in data_list:
    print(data)
