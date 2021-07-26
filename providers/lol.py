import requests
from lxml import html
from bs4 import BeautifulSoup

data = {
    'ime': '',
    'adresa': '',
    'ugovor': '',
    'stanje': ''
}

def fetch(credentials):
    url = "https://www.logosoft.ba/users/services/"
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    payload = {
        "username": credentials['username'],
        "password": credentials['password']
    }

    result = requests.post(url, data=payload, headers=headers)

    soup = BeautifulSoup(result.content, 'html5lib')

    data['ime'] = soup.find(id="mainContent_nazivKorisnika").get_text().strip()
    data['adresa'] = soup.find(id="mainContent_adresaKorisnika").get_text().strip()
    data['stanje'] = soup.find('h3', class_='panel-title', text=credentials['contract']).parent()[2].get_text().strip()
    data['ugovor'] = credentials['contract'].strip()
    return data

def get_table_row(data):
    tabledata = []
    provider = 'Logosoft d.o.o. - Sarajevo'

    description = 'Ugovor: '+data['ugovor']+ \
                '\nKorisnik: '+data['ime']+ \
                '\nAdresa: '+data['adresa']
    state = data['stanje']
    tabledata = [provider,description, state]
    return tabledata


if __name__ == '__main__':
    import config
    credentials = config.credentials['lol']
    data = fetch(credentials)
    print(data)
