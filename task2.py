'''В нашей школе мы не можем разглашать персональные данные пользователей, 
но чтобы преподаватель и ученик смогли объяснить нашей поддержке, кого они имеют в виду (у преподавателей, например, часто учится несколько Саш), 
мы генерируем пользователям уникальные и легко произносимые имена. Имя у нас состоит из прилагательного, имени животного и двузначной цифры. 
В итоге получается, например, "Перламутровый лосось 77". Для генерации таких имен мы и решали следующую задачу:
Получить с русской википедии список всех животных (Категория:Животные по алфавиту) и вывести количество животных на каждую букву алфавита. 
Результат должен получиться в следующем виде:'''

import requests
from bs4 import BeautifulSoup

url = 'https://ru.wikipedia.org/wiki/%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find('span', {'style': 'white-space:nowrap'}).find_all('a')

count = 0
urls = []
for quote in quotes:
    urls.append(quote.attrs['href'])
for url in urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find('div', {'class': 'mw-category-group'}).find_all('li')
    quotes_h3 = soup.find('div', {'class': 'mw-category-group'}).find_all('h3')
    count = 0
    for quote in quotes:
        for h3 in quotes_h3:
            count += 1   
    print(f"{h3.text}:{count}")
