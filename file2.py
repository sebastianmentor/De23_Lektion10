list_of_numbers = [i for i in range(10)]

with open('my_file2.txt', 'w', encoding='utf-8') as file:
    for i in list_of_numbers:
        file.write(f'{i},{i**2},{i**3},{i**4}\n') 

# Vi kan läsa in filer
with open("my_file2.txt","r", encoding="utf-8") as file:
    # Tilldelar variabler
    my_dict = {}
    exponet = ("kvadraten", "kuben", "hyperkuben")
    # Här börja vi läsa i filen
    for line in file.readlines():
        numbers = line.strip().split(",")
        numbers = [int(i) for i in numbers]
        my_dict[numbers[0]] = {
            key:value for key,value in zip(exponet,numbers[1:])
            }
# for key,value in my_dict.items():
#     print(key,"ger",value)
t = my_dict[6]
print(t['kvadraten'],t['kuben'])