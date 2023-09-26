import json

while True:
    val = input('1. Spara meddelande\n2. Avsluta')

    if val == '2': break
    meddeland = input('Skriv ditt meddelande!')

    with open('save_message.json','w', encoding='utf-8') as f:
        lista = list(meddeland)
        dictionary = {}
        for char in lista:
            dictionary[char] = 0

        for letter in meddeland:
            dictionary[letter] += 1
        f.write(json.dumps(dictionary, indent=4))

    with open('save_message.txt','w', encoding='utf-8') as f:
        for key, value in dictionary.items():
            f.write(str(key) + ' antal '+ str(value) + '\n')