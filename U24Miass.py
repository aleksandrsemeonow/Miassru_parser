import requests
from bs4 import BeautifulSoup as bs


headers = {'accept': '*/*',
           'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36'}

Base_URL = 'http://miass.ru/topic.html'


def U24_parser(Base_URL, headers):
    jobs = []
    session = requests.Session()
    request = session.get(Base_URL, headers=headers)
    if request.status_code == 200:
        soup = bs(request.content, 'lxml')
        divs = soup.find_all('div', attrs={'class': 'col-sm-6 col-md-12'})
        for div in divs:
            title = div.find('div', attrs={'class': 'afisha-content__description'}).text
            href = 'http://miass.ru' + div.find('a')['href']
            text = div.find('div', attrs={'class': 'afisha-content__note'}).text
            img = 'http://miass.ru' + div.find('img')['src']
            date = div.find('div', attrs={'class': 'afisha-content__title'}).text
            jobs.append({
                'title': title,
                'href': href,
                'text ': text ,
                'img': img,
                'date': date
            })
        print(len(jobs))
    else:
        print('Error')

U24_parser(Base_URL, headers)