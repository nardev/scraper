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
    session_requests = requests.session()
    url = "https://www.logosoft.ba/users/services/"
    #url = "https://www.logosoft.ba"
    
    # Get login csrf token
    result = session_requests.get(url)
    tree = html.fromstring(result.text)
    payload = {
        "username": credentials['username'],
        "password": credentials['password']
    }

    result = session_requests.post(url, data = payload, headers = dict(referer = url))
    result = session_requests.get(url, headers = dict(referer = url))

    soup = BeautifulSoup(result.content, 'html5lib')
    # val = soup.body.find(id="mainContent_IznosiSvihUgovora").find_all('div')[-1].find_all('span')[0].get_text()

    # box = soup.find(text="Potrošnja u paketu:").find_parent('div').find_all('div', class_='form-group')
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
