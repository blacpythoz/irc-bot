from urllib.request import urlopen
import json

def get_weather(location):
    api_key = "??????????"
    units = "metric"

    try:
        f = urlopen("http://api.openweathermap.org/data/2.5/weather?q=%s&units=metric&appid=85a4e3c55b73909f42c6a23ec35b7147" % location)
        json_string = f.read().decode('utf8')
    except:
        print("Cannot load data")

    parsed_json = json.loads(json_string)

    for keys in parsed_json:
        print(keys," -> ", parsed_json[keys])
    f.close()

get_weather("Chitwan")

