from urllib.request import urlopen
import json

def get_weather(location):
    api_key = "85a4e3c55b73909f42c6a23ec35b7147"
    units = "metric"
    try:
        f = urlopen("http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=85a4e3c55b73909f42c6a23ec35b7147".format(location.title()))
        json_string = f.read().decode('utf8')
        f.close()
    except:
        print("Cannot load data")
        return None
    parsed_json = json.loads(json_string)
    text = "Weather of "+parsed_json['name']+" is: "+parsed_json['weather'][0]['description']+ " with " + str(parsed_json['main']['temp'])+" *C and humidity is "+str(parsed_json['main']['humidity'])
    return text

    #for keys in parsed_json:
        #print(keys," -> ", parsed_json[keys])

#get_weather("Chitwan")

