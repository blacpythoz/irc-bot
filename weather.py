from urllib.request import urlopen
import json

try:
    f = urlopen('http://api.wunderground.com/api/fe5ee2c78e34dacb/geolookup/conditions/q/IA/Cedar_Rapids.json')
    json_string = f.read().decode('utf8')
except:
    print("Cannot load data")

parsed_json = json.loads(json_string)
location = parsed_json['location']['city']
temp_f = parsed_json['current_observation']['temp_f']
#print ("Current temperature in %s is: %s" % (location, temp_f))
for keys in parsed_json:
    print(keys," -> ", parsed_json[keys])
f.close()

