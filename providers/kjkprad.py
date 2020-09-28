import requests
import re
from lxml import html
from bs4 import BeautifulSoup

data = {
    'korisnik':'',
    'adresa':'',
    'ukupno_potrazivanja': '',
    'ukupno_uplate': '',
    'datum': '',
    'stanje': ''
}

def fetch(credentials):
    session_requests = requests.session()

    url = "http://217.199.131.243/afn/fn/"
    login_url = "http://217.199.131.243/afn/fn/wdisp"

    # Get login csrf token
    payload = {
        "login": credentials['username'],
        "passwd": credentials['password'],
        "Register": "Pristup sistemu"
    }

    result = session_requests.post(login_url, data = payload)
    # print(result.headers)
    # print(result.content)
    soup = BeautifulSoup(result.content, 'html.parser')
    cookie = soup.find(src='../images/pix/plus.gif').find_parent('a')['href']
    
    # print(cookie)
    result = session_requests.get(url+cookie)

    soup = BeautifulSoup(result.content, 'html.parser')

    datum = soup.body.find_all(text=re.compile('^Obuhvaćene'))[0]
    cols = soup.body.find(text='U K U P N O:').find_parent('tr').find_all('td')
    iznos = cols[1].get_text().strip()
    uplata = cols[2].get_text().strip()
    dug = cols[3].get_text().strip()

    contact_elements = soup.body.find('table').find('table').find_all('tr')[1].find('span').find_all('span')
    ime = contact_elements[0].get_text().strip()
    adresa = contact_elements[1].get_text()[3:]
    
    data['datum'] = datum
    data['ukupno_potrazivanja'] = iznos
    data['ukupno_uplate'] = uplata
    data['stanje'] = dug
    data['korisnik'] = ime
    data['adresa'] = adresa

    return data

def get_table_row(data):
    tabledata = []
    provider = 'KJKP "RAD" d.o.o.'

    description = 'Korisnik: '+data['korisnik']+ \
        '\nAdresa: '+data['adresa']+ \
        '\nPosljednja Izmjena: '+data['datum']
    state = data['stanje']
    tabledata = [provider,description, state]
    return tabledata

if __name__ == '__main__':
    import config
    credentials = config.credentials['kjkprad']
    data = fetch(credentials)
    # print(data)