# Append till fil 
with open("my_file2.txt",'a') as f:
    i = 10
    f.write(f"{i},{i**2},{i**3},{i**4}\n")

with open("my_file2.txt",'a+') as f:
    i = 11
    f.write(f"{i},{i**2},{i**3},{i**4}\n")
    i = 12
    f.write(f"{i},{i**2},{i**3},{i**4}\n")
    f.seek(0)
    data2 = f.read()

print(data2)