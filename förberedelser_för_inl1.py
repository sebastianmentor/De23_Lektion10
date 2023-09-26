import requests
import json
LONG = '16.545025'
LAT = '59.611366'
URL = f'https://opendata-download-metfcst.smhi.se/api/category/pmp3g/version/2/geotype/point/lon/{LONG}/lat/{LAT}/data.json'
data =  requests.get(URL)

# print(data.status_code)
# with open('sti_data.txt','w') as f:
#     f.write(str(data.content))

if data.status_code == 200:
    print(type(data))

    new_data = data.json()
    print(type(new_data))
    
    # for key in new_data['timeSeries']:
    #     print(key)
    print(type(new_data['timeSeries']))
    print(len(new_data['timeSeries']))

    for key in new_data['timeSeries'][0]['parameters']:
        print(key)