import json

with open('save_message.json','r') as f:
    data = json.load(f)

for key,value in data.items():
    print(f'{key=} --- {value=} {type(value)}')