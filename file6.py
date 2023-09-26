import os

def lägg_till_person_till_fil(person, fil):
    with open(fil, 'a', encoding='utf-8') as f:
        f.write(str(person) + '\n')

def skapa_person() -> dict:

    namnet = input('Skriv in ditt förnamn')
    efternamnet = input('Skriv in ditt efternamn:')
    åldern = int(input('Skriv in din ålder'))
    return dict(namn = namnet, efternamn = efternamnet,ålder = åldern )

def main(lista, FIL):
    while True:
        print('1. Lägg till person!\n2. Skriv ut personer\n3. Avsluta')
        val = input('>>>')

        if val == '1':
            person = skapa_person()
            lägg_till_person_till_fil(person, FIL)   
            lista.append(person)
        elif val == '2':
            for person in lista:
                print(f'{person["namn"]}')
                print(f'{person["efternamn"]}')
                print(f'{person["ålder"]}')
        elif val == '3':
            break




def läs_in_data(file,l):
    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
            lista_med_text = line.strip()
            lista_med_text = lista_med_text.replace('{','').replace('}','')
            lista_med_text = lista_med_text.replace("'",'')
            lista_med_text = lista_med_text.replace(' ','').split(',')
            person = {}
            for item in lista_med_text:
                key, value = item.split(':')
                person[key] = value
            l.append(person)

def start(lista):
    FIL = 'my_save.txt'
    # FIL = 'C:\\Users\\Sebastian\\Systementor\\STI_DE23\\Programmering\\my_save.txt'
    # FIL = r'C:\Users\Sebastian\Systementor\STI_DE23\my_save.txt'
    print(FIL)
    if os.path.exists(FIL):
        läs_in_data(FIL, lista)
    else:
        with open(FIL,'w', encoding='utf-8') as f:
            pass
    main(lista, FIL)


if __name__ == '__main__':
    lista_med_personer = []
    start(lista_med_personer)