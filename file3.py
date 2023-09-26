# Arbeta med json
import json

my_nest = [{1:"1",2:"2",3:"3"}, {"Key":{"key1":"value1","key2":"value2"}}]

with open("my_file3.txt","w") as f:
    f.write(json.dumps(my_nest,indent=2))


with open("my_file3.txt","r") as f:
    data = json.loads(f.read())

print(data)
print(type(data))
print(type(data[0]))
print(type(data[1]['Key']))