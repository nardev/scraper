import requests
from lxml import html
from bs4 import BeautifulSoup

data = {
    'sifra_korisnika': '',
    'adresa': '',
    'posljednja_izmjena': '',
    'stanje': ''
}


def fetch(credentials):
    url = "https://www.epbih.ba/login"
    check_url = "https://www.epbih.ba/profil/mjerna_mjesta"

    session_requests = requests.session()
    result = session_requests.post(url)
    payload = {
        "username": credentials['username'],
        "password": credentials['password']
    }
    result = session_requests.post(url, data = payload, headers = dict(referer = url))
    cookie = result.cookies['ppsession']
    result = session_requests.get(check_url, cookies = dict(result.cookies))
    soup = BeautifulSoup(result.content, 'html5lib')
    # data = soup.body.find('table').find('tbody').find('tr').find_all('td')[2].get_text()
    row = soup.body.find('table').find('tbody').find('tr')
    cols = row.find_all('td')

    data['sifra_korisnika'] = cols[0].find('span')['title'].strip()
    data['adresa'] = cols[0].find('span').get_text().strip()
    data['posljednja_izmjena'] = cols[1].get_text().strip()
    data['stanje'] = cols[2].get_text().strip()
    return data


def get_table_row(data):
    tabledata = []
    provider = 'Elektroprivreda BiH d.d. - Sarajevo.'
    description = 'Sifra korisnika: '+data['sifra_korisnika']+ \
                '\nAdresa: '+data['adresa']+ \
                '\nPosljednja Izmjena: '+data['posljednja_izmjena']
    state = data['stanje']
    tabledata = [provider,description, state]
    return tabledata


if __name__ == '__main__':
    import config
    credentials = config.credentials['epbih']
    data = fetch(credentials)
    print(data)