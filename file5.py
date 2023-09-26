# Enkel felhantering
import os 
data = []
if os.path.exists("my_file22.txt"):
    with open("my_file2.txt", 'r') as f:
        for line in f.readlines():
            data.append(line)
else:
    print('File not found!!!!')
print(data)
# for line in data:
#     print(line, end='')
