import requests
from bs4 import BeautifulSoup as bs


headers = {'accept':'*/*', 
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}


url = 'https://jobs.tut.by/search/vacancy?area=1002&st=searchVacancy&text=python'

def hh(url,headers):
    session = requests.session()
    request = session.get(url, headers=headers)
    if request.status_code ==200:
        soup = bs(request.content, 'html.parser')
        divs = soup.find_all('div', attrs={'data-qa':'vacancy-serp__vacancy vacancy-serp__vacancy_premium'})
        for div in divs:
            title = div.find('a', attrs={'data-qa': "vacancy-serp__vacancy-title"}).text
            href = div.find('a', attrs={'data-qa': "vacancy-serp__vacancy-title"})['href']
            print(href)
    else:
        print('no')
hh(url,headers)
